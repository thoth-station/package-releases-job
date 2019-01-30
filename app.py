#!/usr/bin/env python3
# thoth-package-releases-job
# Copyright(C) 2018 Fridolin Pokorny
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

import logging
import typing

import os
import requests
import yaml

import click
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

from thoth.common import init_logging
from thoth.python import Source
from thoth.storages import GraphDatabase
from thoth.storages import __version__ as thoth_storages_version


# Reuse thoth-storages version as we rely on it.
__version__ = "0.6.0" + "+thoth_storage." + thoth_storages_version


init_logging()

_LOGGER = logging.getLogger("thoth.package_releases")
_PUSH_GATEWAY_HOST = os.getenv("PROMETHEUS_PUSHGATEWAY_HOST")
_PUSH_GATEWAY_PORT = os.getenv("PROMETHEUS_PUSHGATEWAY_PORT")

prometheus_registry = CollectorRegistry()
_METRIC_PACKAGES_NEW_AND_ADDED = Gauge(
    "packages_added", "Packages newly added", registry=prometheus_registry
)
_METRIC_PACKAGES_NEW_AND_NOTIFIED = Gauge(
    "packages_notified",
    "Packages newly added and notification send",
    registry=prometheus_registry,
)
_METRIC_PACKAGES_RELEASES_TIME = Gauge(
    "package_releases_time",
    "Runtime of package releases job",
    registry=prometheus_registry,
)


def _print_version(ctx, _, value):
    """Print package releases version and exit."""
    if not value or ctx.resilient_parsing:
        return
    click.echo(__version__)
    ctx.exit()


def _load_package_monitoring_config(config_path: str) -> typing.Optional[dict]:
    """Load package monitoring configuration, retrieve it from a remote HTTP server if needed."""
    if not config_path:
        return None

    if config_path.startswith(("https://", "http://")):
        _LOGGER.debug(f"Loading remote monitoring config from {config_path}")
        content = requests.get(config_path)
        content.raise_for_status()
        content = content.text
    else:
        _LOGGER.debug(f"Loading local monitoring config from {config_path}")
        with open(config_path, "r") as config_file:
            content = config_file.read()

    return yaml.load(content)


def release_notification(
    monitored_packages: dict, package_name: str, package_version: str
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
            response = requests.post(
                trigger["url"].format(
                    **os.environ,
                    package_name=package_name,
                    package_version=package_version,
                ),
                verify=trigger.get("tls_verify", True),
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
    monitored_packages: dict,
    *,
    graph: GraphDatabase,
    only_if_package_seen: bool = False,
):
    """Check for updates of packages, notify about updates if configured so."""
    sources = [Source(**config) for config in graph.python_package_index_listing()]

    for package_index in sources:
        for package_name in package_index.get_packages():
            try:
                package_versions = package_index.get_package_versions(package_name)
            except Exception as exc:
                _LOGGER.exception("Failed to retrieve package versions for %r: %s", package_name, str(exc))
                continue

            for package_version in package_versions:
                added = graph.create_pypi_package_version(
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

                existed = added[0]
                if not existed:
                    _LOGGER.info(
                        "New release of package %r in version %r hosted on %r added",
                        package_name,
                        package_version,
                        package_index.url,
                    )
                    _METRIC_PACKAGES_NEW_AND_ADDED.inc()
                else:
                    _LOGGER.debug(
                        "Release of %r in version %r hosted on %r already present",
                        package_name,
                        package_version,
                        package_index.url,
                    )

                if added and monitored_packages:
                    try:
                        release_notification(
                            monitored_packages, package_name, package_version
                        )
                        _METRIC_PACKAGES_NEW_AND_NOTIFIED.inc()
                    except Exception as exc:
                        _LOGGER.exception(
                            f"Failed to do release notification for {package_name} ({package_version}), "
                            f"error is not fatal: {str(exc)}"
                        )


@click.command()
@click.pass_context
@click.option("-v", "--verbose", is_flag=True, help="Be verbose about what's going on.")
@click.option(
    "--version",
    is_flag=True,
    is_eager=True,
    callback=_print_version,
    expose_value=False,
    help="Print version and exit.",
)
@click.option(
    "--monitoring-config",
    "-m",
    type=str,
    show_default=True,
    metavar="CONFIG",
    envvar="THOTH_PACKAGE_RELEASES_MONITORING_CONFIG",
    help="PyPI RSS feed to be used.",
)
@click.option(
    "--only-if-package-seen",
    is_flag=True,
    envvar="THOTH_PACKAGE_RELEASES_ONLY_IF_PACKAGE_SEEN",
    help="Create entries only for packages for which entries already exist in the graph database.",
)
def cli(
    ctx=None, verbose=False, monitoring_config: str = None, only_if_package_seen=False
):
    """Check for updates in PyPI RSS feed and add missing entries to the graph database."""
    if ctx:
        ctx.auto_envvar_prefix = "THOTH_PACKAGE_RELEASES"

    if verbose:
        _LOGGER.setLevel(logging.DEBUG)

    _LOGGER.debug("Debug mode turned on")
    _LOGGER.info(f"Package releases version: {__version__}")

    graph = GraphDatabase()
    graph.connect()

    monitored_packages = None
    if monitoring_config:
        try:
            monitored_packages = _load_package_monitoring_config(monitoring_config)
        except Exception:
            _LOGGER.exception(
                f"Failed to load monitoring configuration from {monitoring_config}"
            )
            raise

    try:
        with _METRIC_PACKAGES_RELEASES_TIME.time():
            package_releases_update(
                monitored_packages,
                graph=graph,
                only_if_package_seen=only_if_package_seen,
            )
    finally:
        if _PUSH_GATEWAY_HOST and _PUSH_GATEWAY_PORT:
            try:
                push_gateway = f"{_PUSH_GATEWAY_HOST}:{_PUSH_GATEWAY_PORT}"
                _LOGGER.info(
                    f"Submitting metrics to Prometheus push gateway {push_gateway}"
                )
                push_to_gateway(
                    push_gateway, job="package-releases", registry=prometheus_registry
                )
            except Exception as e:
                _LOGGER.exception(f"An error occurred pushing the metrics: {str(e)}")


if __name__ == "__main__":
    cli()
