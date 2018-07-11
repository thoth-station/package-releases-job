#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
from xml.etree import ElementTree

import os
import requests
import yaml

import click
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

from thoth.common import init_logging
from thoth.storages import GraphDatabase
from thoth.storages import __version__ as thoth_storages_version


__version__ = '0.4.1' + '+thoth_storage.' + thoth_storages_version


init_logging()

_LOGGER = logging.getLogger('thoth.package_releases')
PYPI_RSS_UPDATES = 'https://pypi.org/rss/updates.xml'
_PUSH_GATEWAY_HOST = os.getenv('PROMETHEUS_PUSHGATEWAY_HOST')
_PUSH_GATEWAY_PORT = os.getenv('PROMETHEUS_PUSHGATEWAY_PORT')

prometheus_registry = CollectorRegistry()
_METRIC_PACKAGES_NEW_JUST_DISCOVERED = Gauge(
    'packages_discovereded', 'Packages newly discovered', registry=prometheus_registry)
_METRIC_PACKAGES_NEW_AND_ADDED = Gauge(
    'packages_added', 'Packages newly added', registry=prometheus_registry)
_METRIC_PACKAGES_NEW_AND_NOTIFIED = Gauge(
    'packages_notified', 'Packages newly added and notification send', registry=prometheus_registry)
_METRIC_PACKAGES_RELEASES_TIME = Gauge(
    'package_releases_time', 'Runtime of package releases job', registry=prometheus_registry)


def _print_version(ctx, _, value):
    """Print package releases version and exit."""
    if not value or ctx.resilient_parsing:
        return
    # Reuse thoth-storages version as we rely on it.
    click.echo(__version__)
    ctx.exit()


def get_releases(pypi_rss_feed: str = None) -> list:
    """Get new PyPI releases from PyPI RSS feed. PyPI shows last 40 releases in its feed."""
    _LOGGER.info("Retrieving PyPI RSS feed from %r", pypi_rss_feed)
    response = requests.get(pypi_rss_feed or PYPI_RSS_UPDATES)
    response.raise_for_status()

    tree = ElementTree.fromstring(response.text)
    result = []
    for child in tree.findall('.//channel/item'):
        for item in child.findall('.//link'):
            link = item.text[:-1] if item.text.endswith('/') else item.text
            package_name, package_version = link.rsplit('/', maxsplit=2)[-2:]
            result.append((package_name, package_version))

    return result


def _load_package_monitoring_config(config_path: str) -> typing.Optional[dict]:
    """Load package monitoring configuration, retrieve it from a remote HTTP server if needed."""
    if not config_path:
        return None

    if config_path.startswith(('https://', 'http://')):
        _LOGGER.debug(f"Loading remote monitoring config from {config_path}")
        content = requests.get(config_path)
        content.raise_for_status()
        content = content.text
    else:
        _LOGGER.debug(f"Loading local monitoring config from {config_path}")
        with open(config_path, 'r') as config_file:
            content = config_file.read()

    return yaml.load(content)


def release_notification(monitored_packages: dict, package_name: str) -> bool:
    """Check for release notification in monitoring configuration and trigger notification if requested."""
    was_triggered = False
    for trigger in monitored_packages.get(package_name, {}).get('triggers') or []:
        _LOGGER.debug(f"Triggering release notification for {package_name}")
        try:
            response = requests.post(
                trigger['url'].format(**os.environ),
                verify=trigger.get('tls_verify', True)
            )
            response.raise_for_status()
            was_triggered = True
            _LOGGER.info(
                f"Successfully triggered release notification for {package_name} to {trigger['url']}")
        except Exception as exc:
            _LOGGER.exception(f"Failed to trigger release notification for {package_name} for trigger {trigger}, "
                              f"error is not fatal: {str(exc)}")

    return was_triggered


def package_releases_update(monitored_packages: dict,
                            graph_hosts: str = None, graph_port: int = None, pypi_rss_feed: str = None,
                            only_if_package_seen: bool = False) -> None:
    """Check for PyPI releases and create entries in the graph database if needed."""
    releases = get_releases(pypi_rss_feed=pypi_rss_feed)

    adapter = GraphDatabase(hosts=graph_hosts, port=graph_port)
    adapter.connect()

    for package_name, package_version in releases:
        _LOGGER.debug(
            f"Found release entry in RSS feed for package {package_name} in version {package_version}")
        # We just create an entry in the graph database and let the solver update job do its work. These packages will
        # be orphaned by default as there will be no connection to solver as no solver solved it's dependencies.
        try:
            added = adapter.create_pypi_package_version(
                package_name,
                package_version,
                only_if_package_seen=only_if_package_seen
            )
        except Exception as exc:
            _LOGGER.exception(
                f"Failed to create entry in the graph database for {package_name} "
                f"in version {package_version}: {str(exc)}")
            continue

        _METRIC_PACKAGES_NEW_JUST_DISCOVERED.inc()

        if added:
            _LOGGER.info(
                f"Package {package_name} in version {package_version} was newly added")
            _METRIC_PACKAGES_NEW_AND_ADDED.inc()
        else:
            _LOGGER.info(
                f"Package {package_name} in version {package_version} was not added for tracking")

        if monitored_packages:
            try:
                release_notification(monitored_packages, package_name)

                _METRIC_PACKAGES_NEW_AND_NOTIFIED.inc()
            except Exception as exc:
                _LOGGER.exception(
                    f"Failed to do release notification, error is not fatal: {str(exc)}")


@click.command()
@click.pass_context
@click.option('-v', '--verbose', is_flag=True,
              help="Be verbose about what's going on.")
@click.option('--version', is_flag=True, is_eager=True, callback=_print_version, expose_value=False,
              help="Print version and exit.")
@click.option('--graph-hosts', type=str, metavar=GraphDatabase.ENVVAR_HOST_NAME,
              envvar=GraphDatabase.ENVVAR_HOST_NAME, multiple=True,
              help="Hostname to the graph instance to perform queries for unknown packages.")
@click.option('--graph-port', type=int, metavar='PORT',
              envvar=GraphDatabase.ENVVAR_HOST_PORT,
              help="Port number to the graph instance to perform queries for unknown packages.")
@click.option('--pypi-rss-feed', '-r', type=str, default=PYPI_RSS_UPDATES, show_default=True, metavar='URL',
              help="PyPI RSS feed to be used.")
@click.option('--monitoring-config', '-m', type=str, show_default=True, metavar='CONFIG',
              envvar='THOTH_PACKAGE_RELEASES_MONITORING_CONFIG',
              help="PyPI RSS feed to be used.")
@click.option('--only-if-package-seen', is_flag=True, envvar='THOTH_PACKAGE_RELEASES_ONLY_IF_PACKAGE_SEEN',
              help="Create entries only for packages for which entries already exist in the graph database.")
def cli(ctx=None, verbose=False, pypi_rss_feed=None, monitoring_config: str = None,
        graph_hosts=None, graph_port=None, only_if_package_seen=False):
    """Check for updates in PyPI RSS feed and add missing entries to the graph database."""
    if ctx:
        ctx.auto_envvar_prefix = 'THOTH_PACKAGE_RELEASES'

    if verbose:
        _LOGGER.setLevel(logging.DEBUG)

    _LOGGER.debug("Debug mode turned on")

    monitored_packages = None
    if monitoring_config:
        try:
            monitored_packages = _load_package_monitoring_config(
                monitoring_config)
        except Exception:
            _LOGGER.exception(
                f"Failed to load monitoring configuration from {monitoring_config}")
            raise

    with _METRIC_PACKAGES_RELEASES_TIME.time():
        package_releases_update(
            monitored_packages,
            graph_hosts=graph_hosts,
            graph_port=graph_port,
            pypi_rss_feed=pypi_rss_feed,
            only_if_package_seen=only_if_package_seen
        )

    if _PUSH_GATEWAY_HOST and _PUSH_GATEWAY_PORT:
        try:
            push_to_gateway(f"{push_gateway_host:push_gateway_port}",
                            job='package-releases',
                            registry=prometheus_registry)
        except Exception as e:
            _LOGGER.exception(
                f'An error occurred pushing the metrics: {str(e)}')


if __name__ == '__main__':
    cli()
