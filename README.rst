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

Logic behind new package releases monitoring
============================================

This job checks for package releases on Python package indexes registered to
Thoth's database. The job itself can be configured with in two ways:

* monitor all packages which are available on registered Python package indexes registered in Thoth's knowledge base
* monitor only packages which were previously seen in Thoth

These packages can be "seen" by advises (users of Thoth asked for advise on a
stack with Python packages), provenance checks and/or seen in container image
scans or expertly registered on Management API endpoint. This way Thoth itself
learns what packages are used by users without a need to analyze the whole
PyPI.

Monitoring Python package releases
==================================

This job is also capable of monitoring new Python releases on registered Python
indexes. This is especially useful for triggering internal TensorFlow build
pipeline which is capable of building TensorFlow releases on new upstream
TensorFlow release. These releases are subsequently published on Thoth's Python
package indexes and analyzed by Thoth to give users additional guidance on
software stacks used.

See `config/thoth.yaml` configuration file as an example present in this
repository for more info on configuration options.

Installation and Deployment
===========================

The job is an OpenShift s2i build, the deployment is done via Ansible
playbooks that live in the `core repository
<https://github.com/thoth-station/core>`_.

Running the job locally
=======================

You can run this job locally without a cluster deployment. To do so, prepare your virtual environment and run the script:

.. code-block:: console

  $ pipenv install  # Install all the requirements
  $ pipenv run python3 ./app.py

Job will talk to your local Dgraph instance by default which is located at `localhost:9080` by default. Check `relevant instructions on how to setup a local Dgraph instance <https://github.com/thoth-station/storages#running-dgraph-locally>`_.

If you would like to talk to a cluster instance of Dgraph, you can do so by providing relevant environment variables:

.. code-block:: console

  $ GRAPH_SERVICE_HOST=graph.test.thoth-station.ninja GRAPH_TLS_PATH=./tls-test pipenv run python3 ./app.py

You need to obtain relevant TLS certificates for the cluster deployment you would like to talk to and place them into `./tls-test` directory.

Check documentation for more information on parameters that can be supplied to this job:

.. code-block:: console

  $ pipenv run python3 ./app.py --help
