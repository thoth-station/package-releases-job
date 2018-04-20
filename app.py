#!/usr/bin/env python3

import logging
from xml.etree import ElementTree

import requests

import click

from thoth.common import init_logging
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


def package_releases_update(graph_hosts: str=None, graph_port: int=None, pypi_rss_feed: str=None,
                            only_if_package_seen: bool=False) -> None:
    """Check for PyPI releases and create entries in the graph database if needed."""
    releases = get_releases(pypi_rss_feed=pypi_rss_feed)

    adapter = GraphDatabase(hosts=graph_hosts, port=graph_port)
    adapter.connect()

    for package_name, package_version in releases:
        # We just create an entry in the graph database and let the solver update job do its work. These packages will
        # be orphaned by default as there will be no connection to solver as no solver solved it's dependencies.
        try:
            added = adapter.create_pypi_package_version(
                package_name,
                package_version,
                only_if_package_seen=only_if_package_seen
            )
        except Exception as exc:
            _LOGGER.exception("Failed to create entry in the graph database for %r in version %r: %s",
                              package_name, package_version, str(exc))
            continue

        if added:
            _LOGGER.info("Package %r in version %r was newly added", package_name, package_version)
        else:
            _LOGGER.info("Package %r in version %r was not added for tracking", package_name, package_version)


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
@click.option('--only-if-package-seen', is_flag=True, envvar='THOTH_PACKAGE_RELEASES_ONLY_IF_PACKAGE_SEEN',
              help="Create entries only for packages for which entries already exist in the graph database.")
def cli(ctx=None, verbose=False, pypi_rss_feed=None, graph_hosts=None, graph_port=None, only_if_package_seen=False):
    """Check for updates in PyPI RSS feed and add missing entries to the graph database."""
    if ctx:
        ctx.auto_envvar_prefix = 'THOTH_PACKAGE_RELEASES'

    if verbose:
        _LOGGER.setLevel(logging.DEBUG)

    _LOGGER.debug("Debug mode turned on")

    package_releases_update(
        graph_hosts=graph_hosts,
        graph_port=graph_port,
        pypi_rss_feed=pypi_rss_feed,
        only_if_package_seen=only_if_package_seen
    )


if __name__ == '__main__':
    cli()
