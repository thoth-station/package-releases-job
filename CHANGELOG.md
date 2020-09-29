# Changelog for Thoth's Package Releases Job

## [0.4.0] - 2018-Jul-04 - goern

### Added

New metrics _METRIC_PACKAGES_NEW_AND_NOTIFIED and _METRIC_PACKAGES_RELEASES_TIME, to track 'Packages newly added and notification send' and 'Runtime of package releases job'.

## [0.3.0] - 2018-Jun-30 - goern

### Added

_METRIC_PACKAGES_NEW_AND_ADDED and _METRIC_PACKAGES_NEW_JUST_DISCOVERED metrics are exporte to the pushgateway after each run. The pushgateway is configured via PROMETHEUS_PUSH_GATEWAY which expects `<host>:<port>`.

## [0.2.0] - 2018-Jun-12 - goern

### Added

Set resource limits of BuildConfig and Deployment to reasonable values, this will prevent unpredicted behavior on UpShift.

## Release 0.6.1 (2020-07-08T08:12:36)

- :pushpin: Automatic update of dependency thoth-python from 0.9.2 to 0.10.0 (#432)
- :pushpin: Automatic update of dependency thoth-common from 0.13.8 to 0.14.1 (#431)
- :pushpin: Automatic update of dependency thoth-common from 0.13.8 to 0.14.1 (#430)
- :pushpin: Automatic update of dependency thoth-python from 0.9.2 to 0.10.0 (#428)
- :pushpin: Automatic update of dependency thoth-storages from 0.22.12 to 0.24.0 (#427)
- :pushpin: Automatic update of dependency thoth-common from 0.13.8 to 0.14.1 (#426)
- :pushpin: Automatic update of dependency thoth-storages from 0.22.12 to 0.24.0 (#425)
- :pushpin: Automatic update of dependency requests from 2.23.0 to 2.24.0 (#424)
- include github issue templates (#422)
- Add version to use release pipeline on quay (#420)
- Update OWNERS
- :pushpin: Automatic update of dependency pytest from 5.4.2 to 5.4.3
- added a 'tekton trigger tag_release pipeline issue'
- :pushpin: Automatic update of dependency thoth-common from 0.13.7 to 0.13.8
- :pushpin: Automatic update of dependency thoth-storages from 0.22.11 to 0.22.12
- :pushpin: Automatic update of dependency thoth-common from 0.13.6 to 0.13.7
- :pushpin: Automatic update of dependency prometheus-client from 0.7.1 to 0.8.0
- :pushpin: Automatic update of dependency thoth-common from 0.13.5 to 0.13.6
- :pushpin: Automatic update of dependency thoth-common from 0.13.4 to 0.13.5
- :pushpin: Automatic update of dependency thoth-storages from 0.22.10 to 0.22.11
- :pushpin: Automatic update of dependency thoth-common from 0.13.3 to 0.13.4
- :pushpin: Automatic update of dependency thoth-storages from 0.22.9 to 0.22.10
- :pushpin: Automatic update of dependency pytest from 5.4.1 to 5.4.2
- :pushpin: Automatic dependency re-locking
- :pushpin: Automatic update of dependency thoth-common from 0.13.1 to 0.13.2
- :pushpin: Automatic update of dependency thoth-storages from 0.22.8 to 0.22.9
- :pushpin: Automatic update of dependency thoth-common from 0.13.0 to 0.13.1
- :pushpin: Automatic update of dependency click from 7.1.1 to 7.1.2
- :pushpin: Automatic update of dependency thoth-storages from 0.22.7 to 0.22.8
- :pushpin: Automatic update of dependency thoth-common from 0.12.10 to 0.13.0
- :pushpin: Automatic update of dependency thoth-common from 0.12.9 to 0.12.10
- :pushpin: Automatic update of dependency thoth-python from 0.9.1 to 0.9.2
- :pushpin: Automatic update of dependency thoth-common from 0.12.8 to 0.12.9
- :pushpin: Automatic update of dependency thoth-common from 0.12.7 to 0.12.8
- Remove latest version restriction from .thoth.yaml
- :pushpin: Automatic update of dependency thoth-common from 0.12.6 to 0.12.7
- :pushpin: Automatic update of dependency thoth-common from 0.12.5 to 0.12.6
- :pushpin: Automatic update of dependency thoth-common from 0.12.4 to 0.12.5
- :pushpin: Automatic update of dependency pyyaml from 3.13 to 5.3.1
- :pushpin: Automatic update of dependency thoth-storages from 0.22.6 to 0.22.7
- :pushpin: Automatic update of dependency thoth-storages from 0.22.5 to 0.22.6
- :pushpin: Automatic update of dependency thoth-common from 0.12.3 to 0.12.4
- :pushpin: Automatic update of dependency thoth-common from 0.12.2 to 0.12.3
- :pushpin: Automatic update of dependency thoth-common from 0.12.1 to 0.12.2
- :pushpin: Automatic update of dependency pyyaml from 5.3.1 to 3.13
- :pushpin: Automatic update of dependency thoth-common from 0.12.0 to 0.12.1
- :pushpin: Automatic update of dependency thoth-common from 0.10.12 to 0.12.0
- :pushpin: Automatic update of dependency pyyaml from 3.13 to 5.3.1
- :pushpin: Automatic update of dependency thoth-storages from 0.22.4 to 0.22.5
- :pushpin: Automatic update of dependency thoth-storages from 0.22.3 to 0.22.4
- Read package names from a JSON/YAML file
- :pushpin: Automatic update of dependency thoth-common from 0.10.6 to 0.10.7
- :pushpin: Automatic update of dependency thoth-storages from 0.22.1 to 0.22.2
- :pushpin: Automatic update of dependency thoth-common from 0.10.5 to 0.10.6
- :pushpin: Automatic update of dependency thoth-storages from 0.22.0 to 0.22.1
- :pushpin: Automatic update of dependency thoth-storages from 0.21.11 to 0.22.0
- Update .thoth.yaml
- :pushpin: Automatic update of dependency thoth-common from 0.10.4 to 0.10.5
- :pushpin: Automatic update of dependency thoth-common from 0.10.3 to 0.10.4
- :pushpin: Automatic update of dependency thoth-common from 0.10.2 to 0.10.3
- :pushpin: Automatic update of dependency thoth-common from 0.10.1 to 0.10.2
- :pushpin: Automatic update of dependency thoth-common from 0.10.0 to 0.10.1
- :pushpin: Automatic update of dependency pre-commit from 2.0.0 to 2.0.1
- :pushpin: Automatic update of dependency pytest from 5.3.4 to 5.3.5
- :pushpin: Automatic update of dependency thoth-common from 0.9.31 to 0.10.0
- :pushpin: Automatic update of dependency pre-commit from 1.21.0 to 2.0.0
- :pushpin: Automatic update of dependency thoth-common from 0.9.30 to 0.9.31
- :pushpin: Automatic update of dependency thoth-storages from 0.21.10 to 0.21.11
- :pushpin: Automatic update of dependency thoth-common from 0.9.29 to 0.9.30
- :pushpin: Automatic update of dependency thoth-storages from 0.21.9 to 0.21.10
- :pushpin: Automatic update of dependency thoth-storages from 0.21.8 to 0.21.9
- :pushpin: Automatic update of dependency pytest from 5.3.3 to 5.3.4
- :pushpin: Automatic update of dependency thoth-common from 0.9.28 to 0.9.29
- :pushpin: Automatic update of dependency thoth-storages from 0.21.7 to 0.21.8
- :pushpin: Automatic update of dependency pytest from 5.3.2 to 5.3.3
- :pushpin: Automatic update of dependency thoth-common from 0.9.27 to 0.9.28
- :pushpin: Automatic update of dependency thoth-common from 0.9.26 to 0.9.27
- :pushpin: Automatic update of dependency thoth-storages from 0.21.6 to 0.21.7
- :pushpin: Automatic update of dependency thoth-common from 0.9.25 to 0.9.26
- :pushpin: Automatic update of dependency thoth-storages from 0.21.5 to 0.21.6
- :pushpin: Automatic update of dependency thoth-common from 0.9.24 to 0.9.25
- :pushpin: Automatic update of dependency thoth-storages from 0.21.4 to 0.21.5
- :pushpin: Automatic update of dependency thoth-storages from 0.21.3 to 0.21.4
- Happy new year!
- Use Python package version entity names as a base for known Python packages
- :pushpin: Automatic update of dependency thoth-storages from 0.21.2 to 0.21.3
- :pushpin: Automatic update of dependency thoth-storages from 0.21.1 to 0.21.2
- :pushpin: Automatic update of dependency thoth-common from 0.9.23 to 0.9.24
- :pushpin: Automatic update of dependency thoth-storages from 0.21.0 to 0.21.1
- :pushpin: Automatic update of dependency thoth-storages from 0.20.6 to 0.21.0
- :pushpin: Automatic update of dependency thoth-python from 0.9.0 to 0.9.1
- :pushpin: Automatic update of dependency thoth-python from 0.8.0 to 0.9.0
- :pushpin: Automatic update of dependency thoth-storages from 0.20.5 to 0.20.6
- Do not run adviser from bc in debug mode
- :pushpin: Automatic update of dependency thoth-common from 0.9.22 to 0.9.23
- :pushpin: Automatic update of dependency thoth-storages from 0.20.4 to 0.20.5
- :pushpin: Automatic update of dependency thoth-python from 0.7.1 to 0.8.0
- :pushpin: Automatic update of dependency pyyaml from 5.3b1 to 5.3
- :pushpin: Automatic update of dependency thoth-storages from 0.20.3 to 0.20.4
- :pushpin: Automatic update of dependency thoth-storages from 0.20.2 to 0.20.3
- :pushpin: Automatic update of dependency thoth-storages from 0.20.1 to 0.20.2
- :pushpin: Automatic update of dependency thoth-storages from 0.20.0 to 0.20.1
- :pushpin: Automatic update of dependency pre-commit from 1.20.0 to 1.21.0
- :pushpin: Automatic update of dependency thoth-storages from 0.19.30 to 0.20.0
- :pushpin: Automatic update of dependency pyyaml from 5.2 to 5.3b1
- :pushpin: Automatic update of dependency thoth-storages from 0.19.27 to 0.19.30
- :pushpin: Automatic update of dependency pytest from 5.3.1 to 5.3.2
- :pushpin: Automatic update of dependency thoth-common from 0.9.21 to 0.9.22
- Run package-releases-job twice a day
- Use RHEL instead of UBI
- Update Thoth configuration file and Thoth's s2i configuration
- :pushpin: Automatic update of dependency thoth-storages from 0.19.26 to 0.19.27
- :pushpin: Automatic update of dependency thoth-storages from 0.19.25 to 0.19.26
- Give package-releases job 2 hours to finish
- :pushpin: Automatic update of dependency thoth-common from 0.9.20 to 0.9.21
- :pushpin: Automatic update of dependency thoth-common from 0.9.19 to 0.9.20
- :pushpin: Automatic update of dependency pyyaml from 5.2b1 to 5.2
- :pushpin: Automatic update of dependency thoth-common from 0.9.17 to 0.9.19
- :pushpin: Automatic update of dependency thoth-storages from 0.19.24 to 0.19.25
- :pushpin: Automatic update of dependency thoth-common from 0.9.16 to 0.9.17
- :pushpin: Automatic dependency re-locking
- :pushpin: Automatic update of dependency pytest from 5.3.0 to 5.3.1
- :pushpin: Automatic update of dependency thoth-storages from 0.19.23 to 0.19.24
- :pushpin: Automatic update of dependency thoth-storages from 0.19.22 to 0.19.23
- :pushpin: Automatic update of dependency pytest from 5.2.4 to 5.3.0
- Search only enabled Python indexes
- Use correct query to obtain Python package index configuration
- Check for new releases more often
- Specify image stream registry in cronjob template
- :pushpin: Automatic update of dependency thoth-storages from 0.19.19 to 0.19.22
- :pushpin: Automatic update of dependency pytest from 5.2.3 to 5.2.4
- :pushpin: Automatic update of dependency pytest from 5.2.2 to 5.2.3
- :pushpin: Automatic update of dependency thoth-common from 0.9.15 to 0.9.16
- :pushpin: Automatic update of dependency thoth-common from 0.9.14 to 0.9.15
- :pushpin: Automatic update of dependency thoth-storages from 0.19.18 to 0.19.19
- :pushpin: Automatic update of dependency thoth-storages from 0.19.17 to 0.19.18
- :pushpin: Automatic update of dependency thoth-python from 0.6.5 to 0.7.1
- :pushpin: Automatic update of dependency thoth-storages from 0.19.15 to 0.19.17
- use prometheus collector Registry
- :pushpin: Automatic update of dependency thoth-storages from 0.19.14 to 0.19.15
- Stop using starting deadline seconds
- Fix API Call Error
- :pushpin: Automatic update of dependency thoth-storages from 0.19.12 to 0.19.14
- :pushpin: Automatic update of dependency pre-commit from 1.19.0 to 1.20.0
- :pushpin: Automatic update of dependency black from 19.3b0 to 19.10b0
- updated templates with annotations and param thoth-advise-value
- :pushpin: Automatic update of dependency pre-commit from 1.18.3 to 1.19.0
- :pushpin: Automatic update of dependency thoth-storages from 0.19.11 to 0.19.12
- :pushpin: Automatic update of dependency thoth-storages from 0.19.10 to 0.19.11
- :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
- :pushpin: Automatic update of dependency thoth-python from 0.6.4 to 0.6.5
- :pushpin: Automatic update of dependency thoth-storages from 0.19.9 to 0.19.10
- Fix reversed return value in checks in release monitoring
- Use normalized package names and package versions
- Update query functions according to new naming convention
- :pushpin: Automatic update of dependency thoth-common from 0.9.12 to 0.9.14
- :pushpin: Automatic update of dependency thoth-python from 0.6.3 to 0.6.4
- :pushpin: Automatic update of dependency thoth-common from 0.9.11 to 0.9.12
- :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
- :green_heart: relocked dependencies
- added the standard thoth gitignore file
- :pushpin: Automatic update of dependency thoth-common from 0.9.10 to 0.9.11
- Enhace payload and package releases monitoring handling
- Add untrahook to send package release notifications to
- :pushpin: Automatic update of dependency thoth-storages from 0.19.8 to 0.19.9
- :pushpin: Automatic update of dependency thoth-storages from 0.19.7 to 0.19.8
- :pushpin: Automatic update of dependency thoth-storages from 0.19.6 to 0.19.7
- use postgresql hostname from thoth configmap
- :pushpin: Automatic update of dependency thoth-python from 0.6.2 to 0.6.3
- :pushpin: Automatic update of dependency thoth-storages from 0.19.5 to 0.19.6
- State how to run against local deployment
- :pushpin: Automatic update of dependency thoth-common from 0.9.9 to 0.9.10
- :pushpin: Automatic update of dependency thoth-storages from 0.19.4 to 0.19.5
- :pushpin: Automatic update of dependency thoth-common from 0.9.8 to 0.9.9
- :pushpin: Automatic update of dependency thoth-storages from 0.19.3 to 0.19.4
- :pushpin: Automatic update of dependency thoth-storages from 0.19.2 to 0.19.3
- :pushpin: Automatic update of dependency thoth-storages from 0.19.1 to 0.19.2
- :pushpin: Automatic update of dependency thoth-storages from 0.19.0 to 0.19.1
- :pushpin: Automatic update of dependency thoth-python from 0.6.1 to 0.6.2
- :pushpin: Automatic update of dependency thoth-storages from 0.18.6 to 0.19.0
- Use more generic env var names
- Switch from Dgraph to PostgreSQL in deployment
- Start using Thoth's s2i base image
- Added config
- :pushpin: Automatic update of dependency thoth-storages from 0.18.5 to 0.18.6
- :pushpin: Automatic update of dependency thoth-common from 0.9.7 to 0.9.8
- :pushpin: Automatic update of dependency thoth-common from 0.9.6 to 0.9.7
- Add missing deployment name to template
- :pushpin: Automatic update of dependency thoth-python from 0.6.0 to 0.6.1
- Remove old .thoth.yaml configuration file
- :pushpin: Automatic update of dependency thoth-storages from 0.18.4 to 0.18.5
- Change name of Thoth template to make Coala happy
- Start using Thoth in OpenShift's s2i
- :pushpin: Automatic update of dependency thoth-storages from 0.18.3 to 0.18.4
- :pushpin: Automatic update of dependency thoth-common from 0.9.5 to 0.9.6
- :pushpin: Automatic update of dependency thoth-storages from 0.18.1 to 0.18.3
- :pushpin: Automatic update of dependency thoth-storages from 0.18.0 to 0.18.1
- :pushpin: Automatic update of dependency thoth-storages from 0.17.0 to 0.18.0
- :pushpin: Automatic update of dependency thoth-storages from 0.16.0 to 0.17.0
- :pushpin: Automatic update of dependency thoth-storages from 0.15.2 to 0.16.0
- :pushpin: Automatic update of dependency thoth-common from 0.9.4 to 0.9.5
- :pushpin: Automatic update of dependency thoth-storages from 0.15.1 to 0.15.2
- :pushpin: Automatic update of dependency thoth-python from 0.5.0 to 0.6.0
- :pushpin: Automatic update of dependency thoth-storages from 0.15.0 to 0.15.1
- :pushpin: Automatic update of dependency thoth-storages from 0.14.8 to 0.15.0
- :pushpin: Automatic update of dependency thoth-common from 0.9.3 to 0.9.4
- :pushpin: Automatic update of dependency thoth-storages from 0.14.7 to 0.14.8
- :pushpin: Automatic update of dependency thoth-common from 0.9.2 to 0.9.3
- :pushpin: Automatic update of dependency thoth-storages from 0.14.6 to 0.14.7
- :pushpin: Automatic update of dependency thoth-common from 0.9.1 to 0.9.2
- :pushpin: Automatic update of dependency thoth-storages from 0.14.5 to 0.14.6
- :pushpin: Automatic update of dependency thoth-storages from 0.14.4 to 0.14.5
- Fix issues with old method
- :pushpin: Automatic update of dependency thoth-storages from 0.14.3 to 0.14.4
- :pushpin: Automatic update of dependency thoth-storages from 0.14.2 to 0.14.3
- Standardize environment variables and metrics
- :pushpin: Automatic update of dependency thoth-storages from 0.14.1 to 0.14.2
- Document local usage and some flags
- :pushpin: Automatic update of dependency thoth-common from 0.9.0 to 0.9.1
- Adjust requests and limits
- :pushpin: Automatic update of dependency prometheus-client from 0.7.0 to 0.7.1
- :pushpin: Automatic update of dependency thoth-common from 0.8.11 to 0.9.0
- Update the trigger-build job to use the latest job API
- :pushpin: Automatic update of dependency prometheus-client from 0.6.0 to 0.7.0
- :pushpin: Automatic update of dependency thoth-common from 0.8.7 to 0.8.11
- :pushpin: Automatic update of dependency thoth-storages from 0.14.0 to 0.14.1
- :pushpin: Automatic update of dependency thoth-storages from 0.11.4 to 0.14.0
- :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
- :wrench: fix template for openshift 3.11 and higher
- :pushpin: Automatic update of dependency thoth-common from 0.8.5 to 0.8.7
- :pushpin: Automatic update of dependency thoth-storages from 0.11.3 to 0.11.4
- :pushpin: Automatic update of dependency thoth-storages from 0.11.2 to 0.11.3
- :pushpin: Automatic update of dependency thoth-storages from 0.11.1 to 0.11.2
- :pushpin: Automatic update of dependency thoth-storages from 0.11.0 to 0.11.1
- :pushpin: Automatic update of dependency thoth-storages from 0.10.0 to 0.11.0
- Adjust package-release-job for Dgraph
- :pushpin: Automatic update of dependency thoth-storages from 0.9.7 to 0.10.0
- :pushpin: Automatic update of dependency thoth-common from 0.8.4 to 0.8.5
- Automatic update of dependency thoth-common from 0.8.3 to 0.8.4
- Automatic update of dependency thoth-common from 0.8.2 to 0.8.3
- Automatic update of dependency thoth-common from 0.8.1 to 0.8.2
- Automatic update of dependency thoth-storages from 0.9.6 to 0.9.7
- Automatic update of dependency thoth-python from 0.4.6 to 0.5.0
- Add Thoth's configuration file
- Automatic update of dependency thoth-common from 0.7.1 to 0.8.1
- :bug: fixed the webhook url, using core queue
- :bug: fixed the comment
- :sparkles: added image stream tag and namespace parameter
- Use safe_load for YAML
- Report index against which the package update checks are done
- Check for new package releases daily by default
- Automatic update of dependency prometheus-client from 0.5.0 to 0.6.0
- Automatic update of dependency thoth-common from 0.6.0 to 0.7.1
- Automatic update of dependency thoth-storages from 0.9.5 to 0.9.6
- It's already 2019
- Take into account monitored packages for indexes
- Minor fixes in sources
- Run cronjob every 6 hours
- Add fast path to package retrieval in case of only if seen packages
- Some package versions might be missing on PyPI
- Some packages are not found on index
- Decrease verbosity, we don't need to be notified about packages not added
- Run cronjob once per hour
- Schedule cronjob once per hour
- Use black for formatiing
- Use "existed" flag to notify user about package presence
- Rewrite package release monitoring to use thoth-python
- Do not take graph database configuration explicitly
- Automatic update of dependency thoth-common from 0.5.0 to 0.6.0
- Fix labels - they are part of metadata (#138)
- Automatic update of dependency thoth-storages from 0.9.4 to 0.9.5
- Automatic update of dependency thoth-common from 0.4.6 to 0.5.0
- Automatic update of dependency thoth-storages from 0.9.3 to 0.9.4
- Automatic update of dependency requests from 2.20.1 to 2.21.0
- Automatic update of dependency prometheus-client from 0.4.2 to 0.5.0
- Automatic update of dependency thoth-storages from 0.9.0 to 0.9.3
- Automatic update of dependency thoth-common from 0.4.5 to 0.4.6
- Automatic update of dependency thoth-storages from 0.8.0 to 0.9.0
- Propagate index url into Python package creation
- Automatic update of dependency thoth-common from 0.4.4 to 0.4.5
- Automatic update of dependency thoth-common from 0.4.3 to 0.4.4
- Automatic update of dependency thoth-common from 0.4.2 to 0.4.3
- Automatic update of dependency thoth-common from 0.4.1 to 0.4.2
- Automatic update of dependency thoth-common from 0.4.0 to 0.4.1
- Automatic update of dependency thoth-storages from 0.7.6 to 0.8.0
- Automatic update of dependency requests from 2.20.0 to 2.20.1
- Automatic update of dependency thoth-storages from 0.7.5 to 0.7.6
- Automatic update of dependency thoth-storages from 0.7.4 to 0.7.5
- Automatic update of dependency thoth-storages from 0.7.3 to 0.7.4
- Automatic update of dependency thoth-storages from 0.7.2 to 0.7.3
- Automatic update of dependency thoth-common from 0.3.16 to 0.4.0
- Automatic update of dependency thoth-storages from 0.7.1 to 0.7.2 (#110)
- Automatic update of dependency thoth-common from 0.3.14 to 0.3.16
- Automatic update of dependency thoth-storages from 0.6.0 to 0.7.1
- Automatic update of dependency thoth-common from 0.3.12 to 0.3.14
- Automatic update of dependency thoth-storages from 0.5.4 to 0.6.0
- Automatic update of dependency thoth-common from 0.3.11 to 0.3.12
- Automatic update of dependency requests from 2.19.1 to 2.20.0
- Print version to logs
- Do not catch exception when failed to add new package
- fixing coala issues
- use thoth-* jobs in pipeline
- reviewed all the logging messages to include package name and version
- Automatic update of dependency prometheus-client from 0.4.1 to 0.4.2
- Automatic update of dependency thoth-storages from 0.5.3 to 0.5.4
- Automatic update of dependency thoth-storages from 0.5.2 to 0.5.3
- Automatic update of dependency thoth-common from 0.3.10 to 0.3.11
- added SENTRY_DSN envvar and removed JANUSGRAPH
- Automatic update of dependency thoth-common from 0.3.9 to 0.3.10
- Automatic update of dependency thoth-common from 0.3.8 to 0.3.9
- Automatic update of dependency thoth-common from 0.3.7 to 0.3.8
- Automatic update of dependency prometheus-client from 0.3.1 to 0.4.1
- Automatic update of dependency thoth-common from 0.3.0 to 0.3.7
- Automatic update of dependency click from 6.7 to 7.0
- Update README file
- Automatic update of dependency thoth-common from 0.2.7 to 0.3.0
- removed the jenkinsfile
- better formating
- Automatic update of dependency thoth-common from 0.2.6 to 0.2.7
- Automatic update of dependency thoth-common from 0.2.5 to 0.2.6
- better formating
- Automatic update of dependency thoth-storages from 0.5.1 to 0.5.2
- Automatic update of dependency thoth-common from 0.2.4 to 0.2.5
- Automatic update of dependency thoth-common from 0.2.3 to 0.2.4
- Break URL to conform to line length
- removed zuul queues
- change the queue
- Automatic update of dependency thoth-common from 0.2.2 to 0.2.3
- Automatic update of dependency thoth-storages from 0.5.0 to 0.5.1
- Adjust configuration to trigger release on TF release API
- Expand URL based on package name and package version when triggering
- Trigger package release notification only once
- Automatic update of dependency thoth-storages from 0.4.0 to 0.5.0
- Automatic update of dependency thoth-storages from 0.3.0 to 0.4.0
- Automatic update of dependency thoth-storages from 0.2.0 to 0.3.0
- Automatic update of dependency thoth-storages from 0.1.1 to 0.2.0
- Add metadata to job template
- Automatic update of dependency prometheus-client from 0.3.0 to 0.3.1
- Automatic update of dependency thoth-common from 0.2.1 to 0.2.2
- Automatic update of dependency thoth-storages from 0.1.0 to 0.1.1
- Template default parameter fix
- Template default parameter fix
- Template default parameter fix
- Adjust template labels
- Add CronJob suspend configuration
- Automatic update of dependency thoth-storages from 0.0.33 to 0.1.0
- Update .zuul.yaml
- Update app.py
- Report metrics submission to logs
- fixed the configmap references
- Automatic update of dependency thoth-common from 0.2.0 to 0.2.1 (#53)
- Use Prometheus host and port environment variables when running analyzer
- Automatic update of dependency thoth-common from 0.2.0 to 0.2.1
- Initial dependency lock
- Delete Pipfile.lock for relocking dependencies
- Pin down PyYaml due to aiogremlin version pinning
- using f-strings for all logging
- added a few more metrics
- we dont do travis-ci anymore
- fixing more linters
- Update cronJob-template.yaml
- Add Kebechet to monitored packages to automatically trigger build
- added zuul config
- added zuul config
- added a new metric
- fixed naming of templates
- added yaml to coala glob, fixed template indentation
- Automatically trigger Kebechet build on Kebechet release
- Trigger build webhook for monitored packages
- set resource limits of BC, DC; relocked Pipfile
- Automatic update of dependency thoth-storages from 0.0.28 to 0.0.29
- Automatic update of dependency thoth-storages from 0.0.27 to 0.0.28
- Do not restrict Thoth packages
- Update thoth-common for rsyslog logging
- Add rsyslog logging
- Fix codestyle issue reported
- remove yarl dependency
- default pushgateway and log via LOGGER
- send number of packages added as a gauge to prom push gateway
- Update thoth-storages
- Run coala in CI
- Use coala for code checks
- Update thoth-storages
- Add license header
- Use proper LICENSE file
- OpenShift s2i dir is redundant now
- Enable pipenv on build
- Remove thoth- prefix
- adding the OWNERS file
- Image stream definition was separated
- Separate image stream configuration
- humans: let's reclaim our mattermost channelgit st
- Fix wrong report message
- fixed name of the BC
- fixed name of the BC
- disabled mattermost notification, and created a separate template creation stage
- removed the namespace relationship completely
- build pipeline, is blocked by <https://github.com/thoth-station/package-releases-job/pull/3>
- fixed some naming issues
- added OpenShift templates for CronJob, ImageStream and BuildConfig
- Do not let click handle default options
- Update storages
- Use reStructuredText for README file
- Introduce only if packages seen flag
- Simplify structure to comply s2i app.py
- Add s2i configuration
- Initial project import

## Release 0.7.0 (2020-09-14T17:03:35)
### Features
* Add maintainer (#451)
* make package-release-job a producer (#449)
* enable pre-commit support for the application (#421)
* Remove latest versions limitation (#434)
* migrate manifest for the application to config app (#423)
### Automatic Updates
* :pushpin: Automatic update of dependency pytest from 6.0.0rc1 to 6.0.1 (#445)
* :pushpin: Automatic update of dependency pytest from 6.0.0rc1 to 6.0.1 (#444)
* :pushpin: Automatic update of dependency thoth-python from 0.10.0 to 0.10.1 (#443)
* :pushpin: Automatic update of dependency thoth-common from 0.14.2 to 0.16.1 (#442)
* :pushpin: Automatic update of dependency thoth-storages from 0.24.4 to 0.25.3 (#441)
* :pushpin: Automatic update of dependency pytest from 5.4.3 to 6.0.0rc1 (#439)
* :pushpin: Automatic update of dependency pytest from 5.4.3 to 6.0.0rc1 (#438)
* :pushpin: Automatic update of dependency thoth-common from 0.14.1 to 0.14.2 (#437)
* :pushpin: Automatic update of dependency thoth-common from 0.14.1 to 0.14.2 (#436)
* :pushpin: Automatic update of dependency thoth-storages from 0.24.0 to 0.24.4 (#435)

## Release 0.8.0 (2020-09-14T17:16:31)
### Features
* Release of version 0.7.0 (#455)
* Add maintainer (#451)
* make package-release-job a producer (#449)
* enable pre-commit support for the application (#421)
* Remove latest versions limitation (#434)
* migrate manifest for the application to config app (#423)
* Release of version 0.6.1 (#433)
* include github issue templates (#422)
* Add version to use release pipeline on quay (#420)
* Update OWNERS
* added a 'tekton trigger tag_release pipeline issue'
* :pushpin: Automatic dependency re-locking
* Remove latest version restriction from .thoth.yaml
* Read package names from a JSON/YAML file
* Update .thoth.yaml
* Happy new year!
* Use Python package version entity names as a base for known Python packages
* Run package-releases-job twice a day
* Use RHEL instead of UBI
* Update Thoth configuration file and Thoth's s2i configuration
* Give package-releases job 2 hours to finish
* :pushpin: Automatic dependency re-locking
* Search only enabled Python indexes
* Check for new releases more often
* Specify image stream registry in cronjob template
* Stop using starting deadline seconds
* Fix API Call Error
* updated templates with annotations and param thoth-advise-value
* Fix reversed return value in checks in release monitoring
* Update query functions according to new naming convention
* :green_heart: relocked dependencies
* added the standard thoth gitignore file
* Add untrahook to send package release notifications to
* use postgresql hostname from thoth configmap
* State how to run against local deployment
* Use more generic env var names
* Switch from Dgraph to PostgreSQL in deployment
* Start using Thoth's s2i base image
* Added config
* Add missing deployment name to template
* Remove old .thoth.yaml configuration file
* Start using Thoth in OpenShift's s2i
* Fix issues with old method
* Standardize environment variables and metrics
* Update the trigger-build job to use the latest job API
* Adjust package-release-job for Dgraph
* Add Thoth's configuration file
* :sparkles: added image stream tag and namespace parameter
* Use safe_load for YAML
* Report index against which the package update checks are done
* Check for new package releases daily by default
* It's already 2019
* Take into account monitored packages for indexes
* Run cronjob every 6 hours
* Add fast path to package retrieval in case of only if seen packages
* Some package versions might be missing on PyPI
* Some packages are not found on index
* Decrease verbosity, we don't need to be notified about packages not added
* Run cronjob once per hour
* Schedule cronjob once per hour
* Use black for formatiing
* Use "existed" flag to notify user about package presence
* Do not take graph database configuration explicitly
* Print version to logs
* Do not catch exception when failed to add new package
* Update README file
* change the queue
* Adjust configuration to trigger release on TF release API
* Trigger package release notification only once
* Add metadata to job template
* Adjust template labels
* Add CronJob suspend configuration
* Update .zuul.yaml
* Update app.py
* Report metrics submission to logs
* Use Prometheus host and port environment variables when running analyzer
* Initial dependency lock
* Delete Pipfile.lock for relocking dependencies
* Pin down PyYaml due to aiogremlin version pinning
* Update cronJob-template.yaml
* Add Kebechet to monitored packages to automatically trigger build
* added zuul config
* added zuul config
* added a new metric
* Automatically trigger Kebechet build on Kebechet release
* Trigger build webhook for monitored packages
* set resource limits of BC, DC; relocked Pipfile
* Do not restrict Thoth packages
* Update thoth-common for rsyslog logging
* Add rsyslog logging
* Fix codestyle issue reported
* send number of packages added as a gauge to prom push gateway
* Update thoth-storages
* Run coala in CI
* Update thoth-storages
* Add license header
* Use proper LICENSE file
* OpenShift s2i dir is redundant now
* Enable pipenv on build
* Remove thoth- prefix
* adding the OWNERS file
* Separate image stream configuration
* humans: let's reclaim our mattermost channelgit st
* disabled mattermost notification, and created a separate template creation stage
* build pipeline, is blocked by https://github.com/thoth-station/package-releases-job/pull/3
* added OpenShift templates for CronJob, ImageStream and BuildConfig
* Do not let click handle default options
* Update storages
* Use reStructuredText for README file
* Introduce only if packages seen flag
* Add s2i configuration
* Initial project import
### Bug Fixes
* :wrench: fix template for openshift 3.11 and higher
* :bug: fixed the webhook url, using core queue
* :bug: fixed the comment
* Minor fixes in sources
* fixing coala issues
* Template default parameter fix
* Template default parameter fix
* Template default parameter fix
* fixed the configmap references
* fixing more linters
* fixed naming of templates
* added yaml to coala glob, fixed template indentation
* Image stream definition was separated
* Fix wrong report message
* fixed name of the BC
* fixed name of the BC
* fixed some naming issues
### Improvements
* Do not run adviser from bc in debug mode
* Use correct query to obtain Python package index configuration
* use prometheus collector Registry
* Use normalized package names and package versions
* Enhace payload and package releases monitoring handling
* Change name of Thoth template to make Coala happy
* Document local usage and some flags
* Adjust requests and limits
* Rewrite package release monitoring to use thoth-python
* Fix labels - they are part of metadata (#138)
* Propagate index url into Python package creation
* use thoth-* jobs in pipeline
* reviewed all the logging messages to include package name and version
* added SENTRY_DSN envvar and removed JANUSGRAPH
* removed the jenkinsfile
* better formating
* better formating
* Break URL to conform to line length
* removed zuul queues
* Expand URL based on package name and package version when triggering
* using f-strings for all logging
* added a few more metrics
* we dont do travis-ci anymore
* default pushgateway and log via LOGGER
* removed the namespace relationship completely
* Simplify structure to comply s2i app.py
### Other
* remove yarl dependency
* Use coala for code checks
### Automatic Updates
* :pushpin: Automatic update of dependency pytest from 6.0.0rc1 to 6.0.1 (#445)
* :pushpin: Automatic update of dependency pytest from 6.0.0rc1 to 6.0.1 (#444)
* :pushpin: Automatic update of dependency thoth-python from 0.10.0 to 0.10.1 (#443)
* :pushpin: Automatic update of dependency thoth-common from 0.14.2 to 0.16.1 (#442)
* :pushpin: Automatic update of dependency thoth-storages from 0.24.4 to 0.25.3 (#441)
* :pushpin: Automatic update of dependency pytest from 5.4.3 to 6.0.0rc1 (#439)
* :pushpin: Automatic update of dependency pytest from 5.4.3 to 6.0.0rc1 (#438)
* :pushpin: Automatic update of dependency thoth-common from 0.14.1 to 0.14.2 (#437)
* :pushpin: Automatic update of dependency thoth-common from 0.14.1 to 0.14.2 (#436)
* :pushpin: Automatic update of dependency thoth-storages from 0.24.0 to 0.24.4 (#435)
* :pushpin: Automatic update of dependency thoth-python from 0.9.2 to 0.10.0 (#432)
* :pushpin: Automatic update of dependency thoth-common from 0.13.8 to 0.14.1 (#431)
* :pushpin: Automatic update of dependency thoth-common from 0.13.8 to 0.14.1 (#430)
* :pushpin: Automatic update of dependency thoth-python from 0.9.2 to 0.10.0 (#428)
* :pushpin: Automatic update of dependency thoth-storages from 0.22.12 to 0.24.0 (#427)
* :pushpin: Automatic update of dependency thoth-common from 0.13.8 to 0.14.1 (#426)
* :pushpin: Automatic update of dependency thoth-storages from 0.22.12 to 0.24.0 (#425)
* :pushpin: Automatic update of dependency requests from 2.23.0 to 2.24.0 (#424)
* :pushpin: Automatic update of dependency pytest from 5.4.2 to 5.4.3
* :pushpin: Automatic update of dependency thoth-common from 0.13.7 to 0.13.8
* :pushpin: Automatic update of dependency thoth-storages from 0.22.11 to 0.22.12
* :pushpin: Automatic update of dependency thoth-common from 0.13.6 to 0.13.7
* :pushpin: Automatic update of dependency prometheus-client from 0.7.1 to 0.8.0
* :pushpin: Automatic update of dependency thoth-common from 0.13.5 to 0.13.6
* :pushpin: Automatic update of dependency thoth-common from 0.13.4 to 0.13.5
* :pushpin: Automatic update of dependency thoth-storages from 0.22.10 to 0.22.11
* :pushpin: Automatic update of dependency thoth-common from 0.13.3 to 0.13.4
* :pushpin: Automatic update of dependency thoth-storages from 0.22.9 to 0.22.10
* :pushpin: Automatic update of dependency pytest from 5.4.1 to 5.4.2
* :pushpin: Automatic update of dependency thoth-common from 0.13.1 to 0.13.2
* :pushpin: Automatic update of dependency thoth-storages from 0.22.8 to 0.22.9
* :pushpin: Automatic update of dependency thoth-common from 0.13.0 to 0.13.1
* :pushpin: Automatic update of dependency click from 7.1.1 to 7.1.2
* :pushpin: Automatic update of dependency thoth-storages from 0.22.7 to 0.22.8
* :pushpin: Automatic update of dependency thoth-common from 0.12.10 to 0.13.0
* :pushpin: Automatic update of dependency thoth-common from 0.12.9 to 0.12.10
* :pushpin: Automatic update of dependency thoth-python from 0.9.1 to 0.9.2
* :pushpin: Automatic update of dependency thoth-common from 0.12.8 to 0.12.9
* :pushpin: Automatic update of dependency thoth-common from 0.12.7 to 0.12.8
* :pushpin: Automatic update of dependency thoth-common from 0.12.6 to 0.12.7
* :pushpin: Automatic update of dependency thoth-common from 0.12.5 to 0.12.6
* :pushpin: Automatic update of dependency thoth-common from 0.12.4 to 0.12.5
* :pushpin: Automatic update of dependency pyyaml from 3.13 to 5.3.1
* :pushpin: Automatic update of dependency thoth-storages from 0.22.6 to 0.22.7
* :pushpin: Automatic update of dependency thoth-storages from 0.22.5 to 0.22.6
* :pushpin: Automatic update of dependency thoth-common from 0.12.3 to 0.12.4
* :pushpin: Automatic update of dependency thoth-common from 0.12.2 to 0.12.3
* :pushpin: Automatic update of dependency thoth-common from 0.12.1 to 0.12.2
* :pushpin: Automatic update of dependency pyyaml from 5.3.1 to 3.13
* :pushpin: Automatic update of dependency thoth-common from 0.12.0 to 0.12.1
* :pushpin: Automatic update of dependency thoth-common from 0.10.12 to 0.12.0
* :pushpin: Automatic update of dependency pyyaml from 3.13 to 5.3.1
* :pushpin: Automatic update of dependency thoth-storages from 0.22.4 to 0.22.5
* :pushpin: Automatic update of dependency thoth-storages from 0.22.3 to 0.22.4
* :pushpin: Automatic update of dependency thoth-common from 0.10.6 to 0.10.7
* :pushpin: Automatic update of dependency thoth-storages from 0.22.1 to 0.22.2
* :pushpin: Automatic update of dependency thoth-common from 0.10.5 to 0.10.6
* :pushpin: Automatic update of dependency thoth-storages from 0.22.0 to 0.22.1
* :pushpin: Automatic update of dependency thoth-storages from 0.21.11 to 0.22.0
* :pushpin: Automatic update of dependency thoth-common from 0.10.4 to 0.10.5
* :pushpin: Automatic update of dependency thoth-common from 0.10.3 to 0.10.4
* :pushpin: Automatic update of dependency thoth-common from 0.10.2 to 0.10.3
* :pushpin: Automatic update of dependency thoth-common from 0.10.1 to 0.10.2
* :pushpin: Automatic update of dependency thoth-common from 0.10.0 to 0.10.1
* :pushpin: Automatic update of dependency pre-commit from 2.0.0 to 2.0.1
* :pushpin: Automatic update of dependency pytest from 5.3.4 to 5.3.5
* :pushpin: Automatic update of dependency thoth-common from 0.9.31 to 0.10.0
* :pushpin: Automatic update of dependency pre-commit from 1.21.0 to 2.0.0
* :pushpin: Automatic update of dependency thoth-common from 0.9.30 to 0.9.31
* :pushpin: Automatic update of dependency thoth-storages from 0.21.10 to 0.21.11
* :pushpin: Automatic update of dependency thoth-common from 0.9.29 to 0.9.30
* :pushpin: Automatic update of dependency thoth-storages from 0.21.9 to 0.21.10
* :pushpin: Automatic update of dependency thoth-storages from 0.21.8 to 0.21.9
* :pushpin: Automatic update of dependency pytest from 5.3.3 to 5.3.4
* :pushpin: Automatic update of dependency thoth-common from 0.9.28 to 0.9.29
* :pushpin: Automatic update of dependency thoth-storages from 0.21.7 to 0.21.8
* :pushpin: Automatic update of dependency pytest from 5.3.2 to 5.3.3
* :pushpin: Automatic update of dependency thoth-common from 0.9.27 to 0.9.28
* :pushpin: Automatic update of dependency thoth-common from 0.9.26 to 0.9.27
* :pushpin: Automatic update of dependency thoth-storages from 0.21.6 to 0.21.7
* :pushpin: Automatic update of dependency thoth-common from 0.9.25 to 0.9.26
* :pushpin: Automatic update of dependency thoth-storages from 0.21.5 to 0.21.6
* :pushpin: Automatic update of dependency thoth-common from 0.9.24 to 0.9.25
* :pushpin: Automatic update of dependency thoth-storages from 0.21.4 to 0.21.5
* :pushpin: Automatic update of dependency thoth-storages from 0.21.3 to 0.21.4
* :pushpin: Automatic update of dependency thoth-storages from 0.21.2 to 0.21.3
* :pushpin: Automatic update of dependency thoth-storages from 0.21.1 to 0.21.2
* :pushpin: Automatic update of dependency thoth-common from 0.9.23 to 0.9.24
* :pushpin: Automatic update of dependency thoth-storages from 0.21.0 to 0.21.1
* :pushpin: Automatic update of dependency thoth-storages from 0.20.6 to 0.21.0
* :pushpin: Automatic update of dependency thoth-python from 0.9.0 to 0.9.1
* :pushpin: Automatic update of dependency thoth-python from 0.8.0 to 0.9.0
* :pushpin: Automatic update of dependency thoth-storages from 0.20.5 to 0.20.6
* :pushpin: Automatic update of dependency thoth-common from 0.9.22 to 0.9.23
* :pushpin: Automatic update of dependency thoth-storages from 0.20.4 to 0.20.5
* :pushpin: Automatic update of dependency thoth-python from 0.7.1 to 0.8.0
* :pushpin: Automatic update of dependency pyyaml from 5.3b1 to 5.3
* :pushpin: Automatic update of dependency thoth-storages from 0.20.3 to 0.20.4
* :pushpin: Automatic update of dependency thoth-storages from 0.20.2 to 0.20.3
* :pushpin: Automatic update of dependency thoth-storages from 0.20.1 to 0.20.2
* :pushpin: Automatic update of dependency thoth-storages from 0.20.0 to 0.20.1
* :pushpin: Automatic update of dependency pre-commit from 1.20.0 to 1.21.0
* :pushpin: Automatic update of dependency thoth-storages from 0.19.30 to 0.20.0
* :pushpin: Automatic update of dependency pyyaml from 5.2 to 5.3b1
* :pushpin: Automatic update of dependency thoth-storages from 0.19.27 to 0.19.30
* :pushpin: Automatic update of dependency pytest from 5.3.1 to 5.3.2
* :pushpin: Automatic update of dependency thoth-common from 0.9.21 to 0.9.22
* :pushpin: Automatic update of dependency thoth-storages from 0.19.26 to 0.19.27
* :pushpin: Automatic update of dependency thoth-storages from 0.19.25 to 0.19.26
* :pushpin: Automatic update of dependency thoth-common from 0.9.20 to 0.9.21
* :pushpin: Automatic update of dependency thoth-common from 0.9.19 to 0.9.20
* :pushpin: Automatic update of dependency pyyaml from 5.2b1 to 5.2
* :pushpin: Automatic update of dependency thoth-common from 0.9.17 to 0.9.19
* :pushpin: Automatic update of dependency thoth-storages from 0.19.24 to 0.19.25
* :pushpin: Automatic update of dependency thoth-common from 0.9.16 to 0.9.17
* :pushpin: Automatic update of dependency pytest from 5.3.0 to 5.3.1
* :pushpin: Automatic update of dependency thoth-storages from 0.19.23 to 0.19.24
* :pushpin: Automatic update of dependency thoth-storages from 0.19.22 to 0.19.23
* :pushpin: Automatic update of dependency pytest from 5.2.4 to 5.3.0
* :pushpin: Automatic update of dependency thoth-storages from 0.19.19 to 0.19.22
* :pushpin: Automatic update of dependency pytest from 5.2.3 to 5.2.4
* :pushpin: Automatic update of dependency pytest from 5.2.2 to 5.2.3
* :pushpin: Automatic update of dependency thoth-common from 0.9.15 to 0.9.16
* :pushpin: Automatic update of dependency thoth-common from 0.9.14 to 0.9.15
* :pushpin: Automatic update of dependency thoth-storages from 0.19.18 to 0.19.19
* :pushpin: Automatic update of dependency thoth-storages from 0.19.17 to 0.19.18
* :pushpin: Automatic update of dependency thoth-python from 0.6.5 to 0.7.1
* :pushpin: Automatic update of dependency thoth-storages from 0.19.15 to 0.19.17
* :pushpin: Automatic update of dependency thoth-storages from 0.19.14 to 0.19.15
* :pushpin: Automatic update of dependency thoth-storages from 0.19.12 to 0.19.14
* :pushpin: Automatic update of dependency pre-commit from 1.19.0 to 1.20.0
* :pushpin: Automatic update of dependency black from 19.3b0 to 19.10b0
* :pushpin: Automatic update of dependency pre-commit from 1.18.3 to 1.19.0
* :pushpin: Automatic update of dependency thoth-storages from 0.19.11 to 0.19.12
* :pushpin: Automatic update of dependency thoth-storages from 0.19.10 to 0.19.11
* :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* :pushpin: Automatic update of dependency thoth-python from 0.6.4 to 0.6.5
* :pushpin: Automatic update of dependency thoth-storages from 0.19.9 to 0.19.10
* :pushpin: Automatic update of dependency thoth-common from 0.9.12 to 0.9.14
* :pushpin: Automatic update of dependency thoth-python from 0.6.3 to 0.6.4
* :pushpin: Automatic update of dependency thoth-common from 0.9.11 to 0.9.12
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency thoth-common from 0.9.10 to 0.9.11
* :pushpin: Automatic update of dependency thoth-storages from 0.19.8 to 0.19.9
* :pushpin: Automatic update of dependency thoth-storages from 0.19.7 to 0.19.8
* :pushpin: Automatic update of dependency thoth-storages from 0.19.6 to 0.19.7
* :pushpin: Automatic update of dependency thoth-python from 0.6.2 to 0.6.3
* :pushpin: Automatic update of dependency thoth-storages from 0.19.5 to 0.19.6
* :pushpin: Automatic update of dependency thoth-common from 0.9.9 to 0.9.10
* :pushpin: Automatic update of dependency thoth-storages from 0.19.4 to 0.19.5
* :pushpin: Automatic update of dependency thoth-common from 0.9.8 to 0.9.9
* :pushpin: Automatic update of dependency thoth-storages from 0.19.3 to 0.19.4
* :pushpin: Automatic update of dependency thoth-storages from 0.19.2 to 0.19.3
* :pushpin: Automatic update of dependency thoth-storages from 0.19.1 to 0.19.2
* :pushpin: Automatic update of dependency thoth-storages from 0.19.0 to 0.19.1
* :pushpin: Automatic update of dependency thoth-python from 0.6.1 to 0.6.2
* :pushpin: Automatic update of dependency thoth-storages from 0.18.6 to 0.19.0
* :pushpin: Automatic update of dependency thoth-storages from 0.18.5 to 0.18.6
* :pushpin: Automatic update of dependency thoth-common from 0.9.7 to 0.9.8
* :pushpin: Automatic update of dependency thoth-common from 0.9.6 to 0.9.7
* :pushpin: Automatic update of dependency thoth-python from 0.6.0 to 0.6.1
* :pushpin: Automatic update of dependency thoth-storages from 0.18.4 to 0.18.5
* :pushpin: Automatic update of dependency thoth-storages from 0.18.3 to 0.18.4
* :pushpin: Automatic update of dependency thoth-common from 0.9.5 to 0.9.6
* :pushpin: Automatic update of dependency thoth-storages from 0.18.1 to 0.18.3
* :pushpin: Automatic update of dependency thoth-storages from 0.18.0 to 0.18.1
* :pushpin: Automatic update of dependency thoth-storages from 0.17.0 to 0.18.0
* :pushpin: Automatic update of dependency thoth-storages from 0.16.0 to 0.17.0
* :pushpin: Automatic update of dependency thoth-storages from 0.15.2 to 0.16.0
* :pushpin: Automatic update of dependency thoth-common from 0.9.4 to 0.9.5
* :pushpin: Automatic update of dependency thoth-storages from 0.15.1 to 0.15.2
* :pushpin: Automatic update of dependency thoth-python from 0.5.0 to 0.6.0
* :pushpin: Automatic update of dependency thoth-storages from 0.15.0 to 0.15.1
* :pushpin: Automatic update of dependency thoth-storages from 0.14.8 to 0.15.0
* :pushpin: Automatic update of dependency thoth-common from 0.9.3 to 0.9.4
* :pushpin: Automatic update of dependency thoth-storages from 0.14.7 to 0.14.8
* :pushpin: Automatic update of dependency thoth-common from 0.9.2 to 0.9.3
* :pushpin: Automatic update of dependency thoth-storages from 0.14.6 to 0.14.7
* :pushpin: Automatic update of dependency thoth-common from 0.9.1 to 0.9.2
* :pushpin: Automatic update of dependency thoth-storages from 0.14.5 to 0.14.6
* :pushpin: Automatic update of dependency thoth-storages from 0.14.4 to 0.14.5
* :pushpin: Automatic update of dependency thoth-storages from 0.14.3 to 0.14.4
* :pushpin: Automatic update of dependency thoth-storages from 0.14.2 to 0.14.3
* :pushpin: Automatic update of dependency thoth-storages from 0.14.1 to 0.14.2
* :pushpin: Automatic update of dependency thoth-common from 0.9.0 to 0.9.1
* :pushpin: Automatic update of dependency prometheus-client from 0.7.0 to 0.7.1
* :pushpin: Automatic update of dependency thoth-common from 0.8.11 to 0.9.0
* :pushpin: Automatic update of dependency prometheus-client from 0.6.0 to 0.7.0
* :pushpin: Automatic update of dependency thoth-common from 0.8.7 to 0.8.11
* :pushpin: Automatic update of dependency thoth-storages from 0.14.0 to 0.14.1
* :pushpin: Automatic update of dependency thoth-storages from 0.11.4 to 0.14.0
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* :pushpin: Automatic update of dependency thoth-common from 0.8.5 to 0.8.7
* :pushpin: Automatic update of dependency thoth-storages from 0.11.3 to 0.11.4
* :pushpin: Automatic update of dependency thoth-storages from 0.11.2 to 0.11.3
* :pushpin: Automatic update of dependency thoth-storages from 0.11.1 to 0.11.2
* :pushpin: Automatic update of dependency thoth-storages from 0.11.0 to 0.11.1
* :pushpin: Automatic update of dependency thoth-storages from 0.10.0 to 0.11.0
* :pushpin: Automatic update of dependency thoth-storages from 0.9.7 to 0.10.0
* :pushpin: Automatic update of dependency thoth-common from 0.8.4 to 0.8.5
* Automatic update of dependency thoth-common from 0.8.3 to 0.8.4
* Automatic update of dependency thoth-common from 0.8.2 to 0.8.3
* Automatic update of dependency thoth-common from 0.8.1 to 0.8.2
* Automatic update of dependency thoth-storages from 0.9.6 to 0.9.7
* Automatic update of dependency thoth-python from 0.4.6 to 0.5.0
* Automatic update of dependency thoth-common from 0.7.1 to 0.8.1
* Automatic update of dependency prometheus-client from 0.5.0 to 0.6.0
* Automatic update of dependency thoth-common from 0.6.0 to 0.7.1
* Automatic update of dependency thoth-storages from 0.9.5 to 0.9.6
* Automatic update of dependency thoth-common from 0.5.0 to 0.6.0
* Automatic update of dependency thoth-storages from 0.9.4 to 0.9.5
* Automatic update of dependency thoth-common from 0.4.6 to 0.5.0
* Automatic update of dependency thoth-storages from 0.9.3 to 0.9.4
* Automatic update of dependency requests from 2.20.1 to 2.21.0
* Automatic update of dependency prometheus-client from 0.4.2 to 0.5.0
* Automatic update of dependency thoth-storages from 0.9.0 to 0.9.3
* Automatic update of dependency thoth-common from 0.4.5 to 0.4.6
* Automatic update of dependency thoth-storages from 0.8.0 to 0.9.0
* Automatic update of dependency thoth-common from 0.4.4 to 0.4.5
* Automatic update of dependency thoth-common from 0.4.3 to 0.4.4
* Automatic update of dependency thoth-common from 0.4.2 to 0.4.3
* Automatic update of dependency thoth-common from 0.4.1 to 0.4.2
* Automatic update of dependency thoth-common from 0.4.0 to 0.4.1
* Automatic update of dependency thoth-storages from 0.7.6 to 0.8.0
* Automatic update of dependency requests from 2.20.0 to 2.20.1
* Automatic update of dependency thoth-storages from 0.7.5 to 0.7.6
* Automatic update of dependency thoth-storages from 0.7.4 to 0.7.5
* Automatic update of dependency thoth-storages from 0.7.3 to 0.7.4
* Automatic update of dependency thoth-storages from 0.7.2 to 0.7.3
* Automatic update of dependency thoth-common from 0.3.16 to 0.4.0
* Automatic update of dependency thoth-storages from 0.7.1 to 0.7.2 (#110)
* Automatic update of dependency thoth-common from 0.3.14 to 0.3.16
* Automatic update of dependency thoth-storages from 0.6.0 to 0.7.1
* Automatic update of dependency thoth-common from 0.3.12 to 0.3.14
* Automatic update of dependency thoth-storages from 0.5.4 to 0.6.0
* Automatic update of dependency thoth-common from 0.3.11 to 0.3.12
* Automatic update of dependency requests from 2.19.1 to 2.20.0
* Automatic update of dependency prometheus-client from 0.4.1 to 0.4.2
* Automatic update of dependency thoth-storages from 0.5.3 to 0.5.4
* Automatic update of dependency thoth-storages from 0.5.2 to 0.5.3
* Automatic update of dependency thoth-common from 0.3.10 to 0.3.11
* Automatic update of dependency thoth-common from 0.3.9 to 0.3.10
* Automatic update of dependency thoth-common from 0.3.8 to 0.3.9
* Automatic update of dependency thoth-common from 0.3.7 to 0.3.8
* Automatic update of dependency prometheus-client from 0.3.1 to 0.4.1
* Automatic update of dependency thoth-common from 0.3.0 to 0.3.7
* Automatic update of dependency click from 6.7 to 7.0
* Automatic update of dependency thoth-common from 0.2.7 to 0.3.0
* Automatic update of dependency thoth-common from 0.2.6 to 0.2.7
* Automatic update of dependency thoth-common from 0.2.5 to 0.2.6
* Automatic update of dependency thoth-storages from 0.5.1 to 0.5.2
* Automatic update of dependency thoth-common from 0.2.4 to 0.2.5
* Automatic update of dependency thoth-common from 0.2.3 to 0.2.4
* Automatic update of dependency thoth-common from 0.2.2 to 0.2.3
* Automatic update of dependency thoth-storages from 0.5.0 to 0.5.1
* Automatic update of dependency thoth-storages from 0.4.0 to 0.5.0
* Automatic update of dependency thoth-storages from 0.3.0 to 0.4.0
* Automatic update of dependency thoth-storages from 0.2.0 to 0.3.0
* Automatic update of dependency thoth-storages from 0.1.1 to 0.2.0
* Automatic update of dependency prometheus-client from 0.3.0 to 0.3.1
* Automatic update of dependency thoth-common from 0.2.1 to 0.2.2
* Automatic update of dependency thoth-storages from 0.1.0 to 0.1.1
* Automatic update of dependency thoth-storages from 0.0.33 to 0.1.0
* Automatic update of dependency thoth-common from 0.2.0 to 0.2.1 (#53)
* Automatic update of dependency thoth-common from 0.2.0 to 0.2.1
* Automatic update of dependency thoth-storages from 0.0.28 to 0.0.29
* Automatic update of dependency thoth-storages from 0.0.27 to 0.0.28

## Release 0.8.1 (2020-09-16T06:55:08)
### Features
* run safely (#457)
### Automatic Updates
* :pushpin: Automatic update of dependency thoth-common from 0.18.3 to 0.19.0 (#464)
* :pushpin: Automatic update of dependency thoth-messaging from 0.7.0 to 0.7.2 (#463)
* :pushpin: Automatic update of dependency thoth-common from 0.18.3 to 0.19.0 (#462)
* :pushpin: Automatic update of dependency thoth-common from 0.18.3 to 0.19.0 (#461)
* :pushpin: Automatic update of dependency thoth-storages from 0.25.8 to 0.25.9 (#460)
* :pushpin: Automatic update of dependency thoth-storages from 0.25.8 to 0.25.9 (#459)

## Release 0.8.2 (2020-09-16T15:40:41)
### Features
* :ship: enable aicoe-ci to build and deploy
### Improvements
* make app.sh executable
### Automatic Updates
* :pushpin: Automatic update of dependency thoth-storages from 0.25.9 to 0.25.10 (#473)
* :pushpin: Automatic update of dependency thoth-storages from 0.25.9 to 0.25.10 (#472)
* :pushpin: Automatic update of dependency thoth-messaging from 0.7.0 to 0.7.2 (#468)
* :pushpin: Automatic update of dependency thoth-messaging from 0.7.0 to 0.7.2 (#467)

## Release 0.8.3 (2020-09-16T17:18:53)
### Bug Fixes
* fix import PackageReleasedMessage (#476)
* :wrench: patch fix the aicoe-ci configuration file
### Automatic Updates
* :pushpin: Automatic update of dependency thoth-messaging from 0.7.2 to 0.7.3 (#478)

## Release 0.8.4 (2020-09-23T06:24:23)
### Features
* 📌 Manual update of dependency thoth-messaging from 0.7.3 to 0.7.6 (#482)
### Automatic Updates
* :pushpin: Automatic update of dependency thoth-storages from 0.25.10 to 0.25.11 (#486)
* :pushpin: Automatic update of dependency thoth-storages from 0.25.10 to 0.25.11 (#485)

## Release 0.8.5 (2020-09-24T16:10:19)
### Features
* Be verbose (#493)
### Automatic Updates
* :pushpin: Automatic update of dependency thoth-python from 0.10.1 to 0.10.2 (#491)
* :pushpin: Automatic update of dependency thoth-python from 0.10.1 to 0.10.2 (#490)
* :pushpin: Automatic update of dependency thoth-common from 0.19.0 to 0.20.0 (#489)

## Release 0.8.6 (2020-09-29T08:04:23)
### Bug Fixes
* Send message only of packages that do not exist, not all. (#496)
### Automatic Updates
* :pushpin: Automatic update of dependency thoth-messaging from 0.7.6 to 0.7.7 (#499)
