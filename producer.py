#!/usr/bin/env python3
# thoth-package-releases-job-producer
# Copyright(C) 2018, 2019, 2020 Fridolin Pokorny, Bissenbay Dauletbayev
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

"""Check for new releases on Python index and mark new packages in the graph database."""

import sys
import logging
from typing import Dict, Optional, Any, List

import os
import requests
import yaml

from jsonpath_ng import parse

import click as cli

from version import __version__

from thoth.common import __version__ as __common__version__
from thoth.common import init_logging

from thoth.storages import __version__ as __storages__version__
from thoth.storages import GraphDatabase

from thoth.messaging import __version__ as __messaging__version__
import thoth.messaging.producer as producer
from thoth.messaging import package_released_message
from thoth.messaging.package_releases import MessageContents as PackageReleasedContent

from prometheus_client import CollectorRegistry, Gauge, Counter, push_to_gateway

from thoth.python import Source
from thoth.python.exceptions import NotFound

init_logging()

prometheus_registry = CollectorRegistry()

p = producer.create_producer()

_LOGGER = logging.getLogger("thoth.package_releases_job")
__service_version__ = f"{__version__}+storages.{__storages__version__}.common.{__common__version__}.messaging.{__messaging__version__}"  # noqa: E501
_LOGGER.info("Thoth-package-releases-job-producer v%s", __service_version__)

_THOTH_DEPLOYMENT_NAME = os.environ["THOTH_DEPLOYMENT_NAME"]
_THOTH_METRICS_PUSHGATEWAY_URL = os.getenv("PROMETHEUS_PUSHGATEWAY_URL")

COMPONENT_NAME = "thoth-package-releases-job"

# Metrics Exporter Metrics
_METRIC_INFO = Gauge(
    "thoth_package_release_job_info",
    "Thoth Package Release Producer information",
    ["env", "version"],
    registry=prometheus_registry,
)

_METRIC_MESSSAGES_SENT = Counter(
    "thoth_package_release_job_messages_sent",
    "Thoth Package Release Producer information sent",
    ["message_type", "env", "version"],
    registry=prometheus_registry,
)

_METRIC_DATABASE_SCHEMA_SCRIPT = Gauge(
    "thoth_database_schema_revision_script",
    "Thoth database schema revision from script",
    ["component", "revision", "env"],
    registry=prometheus_registry,
)

_METRIC_INFO.labels(_THOTH_DEPLOYMENT_NAME, __service_version__).inc()

_METRIC_DATABASE_SCHEMA_SCRIPT.labels(
    COMPONENT_NAME,
    GraphDatabase().get_script_alembic_version_head(),
    _THOTH_DEPLOYMENT_NAME,
).inc()


def _print_version(ctx, _, value) -> None:
    """Print package releases version and exit."""
    if not value or ctx.resilient_parsing:
        return
    ctx.exit()


def _load_package_monitoring_config(config_path: str) -> Optional[Dict[Any, Any]]:
    """Load package monitoring configuration, retrieve it from a remote HTTP server if needed."""
    if not config_path:
        return None

    if config_path.startswith(("https://", "http://")):
        _LOGGER.debug(f"Loading remote monitoring config from {config_path}")
        content = requests.get(config_path)
        content.raise_for_status()
        content_info = content.text
    else:
        _LOGGER.debug(f"Loading local monitoring config from {config_path}")
        with open(config_path, "r") as config_file:
            content_info = config_file.read()

    return yaml.safe_load(content_info)


def release_notification(
    monitored_packages: dict, package_name: str, package_version: str, index_url: str
) -> bool:
    """Check for release notification in monitoring configuration and trigger notification if requested."""
    was_triggered = False
    for trigger in monitored_packages.get(package_name, {}).get("triggers") or []:
        _LOGGER.debug(
            f"Triggering release notification for {package_name} ({package_version})"
        )
        try:
            # We expand URL based on environment variables, package name and package version so a user can fully
            # configure what should be present in the URL.
            kwargs = {}
            if trigger["url"].startswith("https://"):
                kwargs["verify"] = trigger.get("tls_verify", True)

            response = requests.post(
                trigger["url"].format(
                    **os.environ,
                    package_name=package_name,
                    package_version=package_version,
                    index_url=index_url,
                    thoth_deployment_name=_THOTH_DEPLOYMENT_NAME,
                ),
                data={
                    "package_name": package_name,
                    "package_version": package_version,
                    "index_url": index_url,
                    "thoth_deployment_name": _THOTH_DEPLOYMENT_NAME,
                },
                **kwargs,
            )
            response.raise_for_status()
            was_triggered = True
            _LOGGER.info(
                f"Successfully triggered release notification for {package_name} "
                f"({package_version}) to {trigger['url']}"
            )
        except Exception as exc:
            _LOGGER.exception(
                f"Failed to trigger release notification for {package_name} "
                f"({package_version}) for trigger {trigger}, error is not fatal: {str(exc)}"
            )

    return was_triggered


def package_releases_update(
    monitored_packages: Optional[dict],
    *,
    graph: GraphDatabase,
    package_names: Optional[List[str]] = None,
) -> int:
    """Check for updates of packages, notify about updates if configured so."""
    sources = []
    for index_config in graph.get_python_package_index_all(enabled=True):
        only_if_package_seen = index_config.pop("only_if_package_seen", True)
        source = Source(
            url=index_config["url"],
            warehouse_api_url=index_config["warehouse_api_url"],
            verify_ssl=index_config["verify_ssl"],
        )
        sources.append((source, only_if_package_seen))

    package_releases_messages_sent = 0

    for package_index, only_if_package_seen in sources:
        _LOGGER.info("Checking index %r for new package releases", package_index.url)
        for package_name in package_names or package_index.get_packages():
            try:
                package_versions = package_index.get_package_versions(package_name)
            except NotFound as exc:
                _LOGGER.debug(
                    "No versions found for package %r on %r: %s",
                    package_name,
                    package_index.url,
                    str(exc),
                )
                continue
            except Exception as exc:
                _LOGGER.exception(
                    "Failed to retrieve package versions for %r: %s",
                    package_name,
                    str(exc),
                )
                continue

            for package_version in package_versions:
                added = graph.create_python_package_version_entity(
                    package_name,
                    package_version,
                    package_index.url,
                    only_if_package_seen=only_if_package_seen,
                )

                if added is None:
                    _LOGGER.debug(
                        "Package %r in version %r hosted on %r was not added - it was not previously seen",
                        package_name,
                        package_version,
                        package_index.url,
                    )
                    continue

                existed = added[1]
                if not existed:
                    _LOGGER.info(
                        "New release of package %r in version %r hosted on %r added",
                        package_name,
                        package_version,
                        package_index.url,
                    )

                    producer.publish_to_topic(
                        p,
                        package_released_message,
                        PackageReleasedContent(
                            package_name=package_name,
                            package_version=package_version,
                            index_url=package_index.url,
                            component_name=COMPONENT_NAME,
                            service_version=__service_version__,
                        ),
                    )

                    _LOGGER.debug(
                        "Package %r in version %r hosted on %r added to list to be sent as Kafka message %r",
                        package_name,
                        package_version,
                        package_index.url,
                        package_released_message.topic_name,
                    )
                    package_releases_messages_sent += 1
                else:
                    _LOGGER.debug(
                        "Release of %r in version %r hosted on %r already present",
                        package_name,
                        package_version,
                        package_index.url,
                    )

                if added and monitored_packages:
                    entity = added[0]
                    try:
                        release_notification(
                            monitored_packages,
                            entity.package_name,
                            entity.package_version,
                            package_index.url,
                        )
                    except Exception as exc:
                        _LOGGER.exception(
                            f"Failed to do release notification for {package_name} ({package_version} "
                            f"from {package_index.url}), error is not fatal: {str(exc)}"
                        )
    p.flush()
    return package_releases_messages_sent


@cli.command()
@cli.option(
    "-v",
    "--verbose",
    is_flag=True,
    envvar="THOTH_PACKAGE_RELEASES_DEBUG",
    help="Be verbose about what's going on.",
)
@cli.option(
    "--version",
    is_flag=True,
    is_eager=True,
    callback=_print_version,
    expose_value=False,
    help="Print version and exit.",
)
@cli.option(
    "--monitoring-config",
    "-m",
    type=str,
    show_default=True,
    metavar="CONFIG",
    envvar="THOTH_PACKAGE_RELEASES_MONITORING_CONFIG",
    help="A filesystem path or an URL to monitoring configuration file.",
)
@cli.option(
    "--package-names-file",
    "-f",
    type=str,
    metavar="FILE.json",
    envvar="THOTH_PACKAGE_RELEASES_PACKAGE_NAMES_FILE",
    help="A path to a JSON file that stores information about package names, "
    "disjoint with `--only-if-package-seen`.",
)
@cli.option(
    "--package-names-file-jsonpath",
    type=str,
    metavar="JSONPATH",
    envvar="THOTH_PACKAGE_RELEASES_PACKAGE_NAMES_FILE_JSONPATH",
    help="A path to a JSON/YAML file that stores information about package names, "
    "disjoint with `--only-if-package-seen`.",
)
def main(
    ctx=None,
    verbose: bool = False,
    monitoring_config: Optional[str] = None,
    package_names_file: Optional[str] = None,
    package_names_file_jsonpath: Optional[str] = None,
):
    """Check for updates in PyPI RSS feed and add missing entries to the graph database."""
    if ctx:
        ctx.auto_envvar_prefix = "THOTH_PACKAGE_RELEASES"

    if verbose:
        _LOGGER.setLevel(logging.DEBUG)

    _LOGGER.debug("Debug mode turned on")
    _LOGGER.info("Package releases version: %r", __version__)

    if package_names_file_jsonpath and not package_names_file:
        raise ValueError("Cannot use JSON path when no package names file provided")

    if not package_names_file_jsonpath and package_names_file:
        raise ValueError(
            "JSON path required when obtaining package names from a JSON file"
        )

    package_names = None
    if package_names_file:
        with open(package_names_file, "r") as f:
            content = yaml.safe_load(f)

        package_names = []
        for item in parse(package_names_file_jsonpath).find(content):
            for entry in item.value:
                if not isinstance(entry, str):
                    raise ValueError(
                        f"Found item in the file is not a string describing package name: {item!r}"
                    )
                package_names.append(entry)

        if not package_names:
            _LOGGER.warning("No packages to be checked for new releases")
            sys.exit(2)

    # Connect once we really need to.
    graph = GraphDatabase()
    graph.connect()

    # An optimization - we don't need to iterate over a large set present on index.
    # Check only packages known to Thoth based on index configuration.
    package_names = graph.get_python_package_version_entities_names_all()

    monitored_packages = None
    if monitoring_config:
        try:
            monitored_packages = _load_package_monitoring_config(monitoring_config)
        except Exception:
            _LOGGER.exception(
                f"Failed to load monitoring configuration from {monitoring_config}"
            )
            raise

    package_releases_messages_sent = package_releases_update(
        monitored_packages,
        graph=graph,
        package_names=package_names,
    )

    _METRIC_MESSSAGES_SENT.labels(
        message_type=package_released_message.topic_name,
        env=_THOTH_DEPLOYMENT_NAME,
        version=__service_version__,
    ).inc(package_releases_messages_sent)

    if _THOTH_METRICS_PUSHGATEWAY_URL:
        try:
            _LOGGER.debug(
                f"Submitting metrics to Prometheus pushgateway {_THOTH_METRICS_PUSHGATEWAY_URL}"
            )
            push_to_gateway(
                _THOTH_METRICS_PUSHGATEWAY_URL,
                job="package-releases",
                registry=prometheus_registry,
            )
        except Exception as e:
            _LOGGER.exception(f"An error occurred pushing the metrics: {str(e)}")


if __name__ == "__main__":
    main()
