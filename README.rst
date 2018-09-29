thoth-package-releases-job
--------------------------

A job for monitoring new releases on Python package indexes such as the
`public PyPI <https://pypi.org>`_ and creating relevant entries in the graph
database.

This job is run periodically as an OpenShift CronJob. The job checks for
updates of packages that are released on PyPI. These updates are monitored
via PyPI's `RSS feed <https://pypi.org/rss/updates.xml>`_ that lists the most
recently updated packages. If a newly released package is known to Thoth (it
was previously analyzed or used in any runtime/buildtime environment), this
job creates an entry in the graph database. The actual scheduling of analyses
of the newly released package is done using `graph-refresh-job
<https://github.com/thoth-station/graph-refresh-job>`_.

Installation and Deployment
===========================

The job is an OpenShift s2i build, the deployment is done via Ansible
playbooks that live in the `core repository
<https://github.com/thoth-station/core>`_.
