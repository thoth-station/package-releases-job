#!/usr/bin/env python3

import logging
from xml.etree import ElementTree

import requests

import click

from thoth.common import init_logging
from thoth.storages.graph.models import HasVersion
from thoth.storages.graph.models import Package
from thoth.storages.graph.models import PythonPackageVersion
from thoth.storages import GraphDatabase
from thoth.storages import __version__

init_logging()

_LOGGER = logging.getLogger('thoth.package_releases')
PYPI_RSS_UPDATES = 'https://pypi.org/rss/updates.xml'


def _print_version(ctx, _, value):
    """Print package releases version and exit."""
    if not value or ctx.resilient_parsing:
        return
    # Reuse thoth-storages version as we rely on it.
    click.echo(__version__)
    ctx.exit()


def get_releases(pypi_rss_feed: str=None) -> list:
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


def package_releases_update(graph_hosts: str=None, graph_port: int=None, pypi_rss_feed: str=None) -> None:
    """Check for PyPI releases and create entries in the graph database if needed."""
    releases = get_releases(pypi_rss_feed=pypi_rss_feed)

    _LOGGER.debug("Connecting to the graph database, host %r and port %d", graph_hosts, graph_port)
    adapter = GraphDatabase(hosts=graph_hosts, port=graph_port)
    adapter.connect()

    for package_name, package_version in releases:
        # We just create an entry in the graph database and let the solver update job do its work. These packages will
        # be orphaned by default as there will be no connection to solver as no solver solved it's dependencies.
        try:
            # TODO: we could move this logic to thoth-storages to have this at one place
            _LOGGER.debug("Checking package entry %r in the graph database", package_name)
            python_package = Package.from_properties(
                ecosystem='pypi',
                package_name=package_name
            )
            existed = python_package.get_or_create(adapter.g)
            if existed:
                _LOGGER.debug("Package entry %r already existed in the graph database", package_name)
            else:
                _LOGGER.debug("Package entry %r has been added to the graph database", package_name)

            _LOGGER.debug("Checking %r in version %r in the graph database", package_name, package_version)
            python_package_version = PythonPackageVersion.from_properties(
                ecosystem='pypi',
                package_name=package_name,
                package_version=package_version
            )
            existed = python_package_version.get_or_create(adapter.g)

            HasVersion.from_properties(
                source=python_package,
                target=python_package_version
            ).get_or_create(adapter.g)
        except Exception as exc:
            _LOGGER.exception("Failed to create entry in the graph database for %r in version %r: %s",
                              package_name, package_version, str(exc))
            continue

        if not existed:
            _LOGGER.info("Package %r in version %r was newly added", package_name, package_version)
        else:
            _LOGGER.info("Package %r in version %r was already present in the graph database",
                         package_name, package_version)


@click.group()
@click.pass_context
@click.option('-v', '--verbose', is_flag=True,
              help="Be verbose about what's going on.")
@click.option('--version', is_flag=True, is_eager=True, callback=_print_version, expose_value=False,
              help="Print version and exit.")
def cli(ctx=None, verbose=0):
    """Check upstream releases and create entries in the graph database for the new ones."""
    if ctx:
        ctx.auto_envvar_prefix = 'THOTH_PACKAGE_RELEASES'

    if verbose:
        _LOGGER.setLevel(logging.DEBUG)
        _LOGGER.debug("Debug mode turned on")


@cli.command()
@click.option('--graph-hosts', type=str, default=[GraphDatabase.DEFAULT_HOST],
              show_default=True, metavar=GraphDatabase.ENVVAR_HOST_NAME,
              envvar=GraphDatabase.ENVVAR_HOST_NAME, multiple=True,
              help="Hostname to the graph instance to perform queries for unknown packages.")
@click.option('--graph-port', type=int, default=GraphDatabase.DEFAULT_PORT, show_default=True, metavar='PORT',
              envvar=GraphDatabase.ENVVAR_HOST_PORT,
              help="Port number to the graph instance to perform queries for unknown packages.")
@click.option('--pypi-rss-feed', '-r', type=str, default=PYPI_RSS_UPDATES, show_default=True, metavar='URL',
              help="PyPI RSS feed to be used.")
def pypi(pypi_rss_feed=None, graph_hosts=None, graph_port=None):
    """Check for updates in PyPI RSS feed and add missing entries to the graph database."""
    package_releases_update(graph_hosts=graph_hosts, graph_port=graph_port, pypi_rss_feed=pypi_rss_feed)


if __name__ == '__main__':
    cli()
