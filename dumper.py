#!/usr/bin/env python3
# webhook2kafka
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


"""This will send all the webhook payloads to a Kafka topic."""

import os
import sys
import ssl
import logging
import json


import faust


from thoth.common import init_logging
from thoth.messaging import PackageRelease, THOTH_PACKAGE_RELEASES_TOPIC_NAME


__version__ = "0.1.0-dev"

_DEBUG = os.getenv("DEBUG", False)


init_logging()
_LOGGER = logging.getLogger("dumper")
_LOGGER.setLevel(logging.DEBUG if _DEBUG else logging.INFO)

_KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
_KAFKA_CAFILE = os.getenv("KAFKA_CAFILE", "secrets/data-hub-kafka-ca.crt")
_KAFKA_TOPIC_RETENTION_TIME_SECONDS = 60 * 60 * 24 * 45


ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=_KAFKA_CAFILE)
app = faust.App("thoth_package_releases", broker=_KAFKA_BOOTSTRAP_SERVERS, ssl_context=ssl_context, web_enabled=False)
package_releases_topic = app.topic(
    THOTH_PACKAGE_RELEASES_TOPIC_NAME,
    value_type=PackageRelease,
    retention=_KAFKA_TOPIC_RETENTION_TIME_SECONDS,
    partitions=1,
)


@app.agent(package_releases_topic)
async def dump(releases):
    """Dump the messages received."""
    async for release in releases:
        print(f"{release}")


if __name__ == "__main__":
    _LOGGER.info(f"Package Releases dumper v{__version__} started.")
    _LOGGER.debug("DEBUG mode is enabled!")

    app.main()
