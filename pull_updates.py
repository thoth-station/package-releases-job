#!/usr/bin/env python3
# pull_updates ٩(◕‿◕)۶
# Copyright(C) 2019 Christoph Görn
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""This will pull updated Python Package Releases and send them to a Kafka topic."""


import os
import sys
import ssl
import logging
import json

import aiohttp
import faust

from http import HTTPStatus
from mode import Service

from thoth.common import init_logging
from thoth.common import __version__ as thoth_common_version
from thoth.python import AIOSource
from thoth.python import __version__ as thoth_python_version
from thoth.python.exceptions import NotFound
from thoth.storages import GraphDatabase
from thoth.storages import __version__ as thoth_storages_version
from thoth.messaging import THOTH_PACKAGE_RELEASES_TOPIC_NAME, PackageRelease, __version__ as thoth_messaging_version


__version__ = (
    f"0.7.0-dev+thoth_storage.{thoth_storages_version}+thoth_python."
    f"{thoth_python_version}+thoth_messaging.{thoth_messaging_version}"
)


init_logging()


_DEBUG = os.getenv("DEBUG", False)
_LOGGER = logging.getLogger("pull_updates")
_LOGGER.setLevel(logging.DEBUG if _DEBUG else logging.INFO)

_KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
_KAFKA_CAFILE = os.getenv("KAFKA_CAFILE", "secrets/data-hub-kafka-ca.crt")
_KAFKA_TOPIC_RETENTION_TIME_SECONDS = 60 * 60 * 24 * 45  # seconds
_PULL_UPDATES_TIMER_SLEEP_SECONDS = os.getenv("PULL_UPDATES_TIMER_SLEEP", 60 * 5)


graph = None

ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=_KAFKA_CAFILE)
app = faust.App(
    "thoth_package_releases",
    broker=_KAFKA_BOOTSTRAP_SERVERS,
    value_serializer="json",
    ssl_context=ssl_context,
    web_enabled=True,
    web_bind="0.0.0.0",
    web_port=8080,
)

package_releases_topic = app.topic(
    THOTH_PACKAGE_RELEASES_TOPIC_NAME,
    value_type=PackageRelease,
    retention=_KAFKA_TOPIC_RETENTION_TIME_SECONDS,
    partitions=1,
    internal=True,
)


@app.task()
async def connect_graph():
    """Connect to Thoth's Knowledge Graph."""
    global graph

    graph = GraphDatabase()
    graph.connect()
    _LOGGER.info(f"connected to Thoth's Knowledge Graph using thoth.storages v{thoth_storages_version} ...")


@app.page("/healthz")
async def healthz(web, request):
    """Give some health information."""
    global graph

    if graph is None:
        return (
            web.json({"status": "bad", "version": __version__, "message": "Thoth's Knowledge Graph is not connected!"}),
            503,
        )

    if graph.is_connected:
        return web.json({"status": "ok", "version": __version__})
    else:
        return (
            web.json({"status": "bad", "version": __version__, "message": "Thoth's Knowledge Graph is not connected!"}),
            503,
        )


@app.timer(interval=_PULL_UPDATES_TIMER_SLEEP_SECONDS)
async def pull_updates_timer(self):
    """Go and look for updates of all packages on all known indices."""
    _LOGGER.debug("pull_updates_timer Task woke up")

    if not graph.is_connected():
        _LOGGER.error("Thoth's Knowledge Graph is not connected!")

    # get all the Indicies known to Thoth
    sources = [AIOSource(**config) for config in graph.get_python_package_index_all()]

    _LOGGER.debug(f"checking indices: {sources}")

    for package_index in sources:
        _LOGGER.info("Checking index %r for new package releases", package_index.url)

        packages = await package_index.get_packages()
        async for package_name in packages:
            _LOGGER.info(f"checking '{package_name}' for new releases")

            try:
                package_versions = await package_index.get_package_versions(package_name)
            except NotFound as exc:
                _LOGGER.debug("No versions found for package %r on %r: %s", package_name, package_index.url, str(exc))
                continue
            except Exception as exc:
                _LOGGER.exception("Failed to retrieve package versions for %r: %s", package_name, str(exc))
                continue

            async for package_version in package_versions:
                # let's add the package_version and check if it existed before....
                added = graph.create_python_package_version_entity(
                    package_name, package_version, package_index.url, only_if_package_seen=0
                )
                existed = added[1]

                if added is None:
                    _LOGGER.debug(
                        "Package %r in version %r hosted on %r was not added - it was not previously seen",
                        package_name,
                        package_version,
                        package_index.url,
                    )
                    continue

                if not existed:
                    _LOGGER.info(
                        "New release of package %r in version %r hosted on %r added",
                        package_name,
                        package_version,
                        package_index.url,
                    )

                    await package_releases_topic.send(
                        value=PackageRelease(package_index.url, package_name, package_version)
                    )
                else:
                    _LOGGER.debug(
                        "Release of %r in version %r hosted on %r already present",
                        package_name,
                        package_version,
                        package_index.url,
                    )


if __name__ == "__main__":
    _LOGGER.info(f"Package Releases Pull Updates v{__version__} started.")
    _LOGGER.debug("DEBUG mode is enabled!")

    app.main()
