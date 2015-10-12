# Master_Project_Infrastructure

This project is to construct all of the infrastructure of the Master Project of Snaplogic Monitor System. 

# DESRIPTIOIN #

This goal of this infrastructure project:
- Construct a kafka-cluster to ingest and consume data.
- Construct a hadoop and spark cluster to analyze data realtime.
- Build a web server to show data on dashboard.

In this project we use docker container to depoly all service and use maestro-ng to integrate all service.

# REQUIREMENTS #

- All of the nodes in the cluster have to run a docker daemon on it.
- The host computer have to install the maestro-ng.

# USAGE #

- Change the maestro.yaml file to configure your cluster information.
- Run maestro by this yaml file.
