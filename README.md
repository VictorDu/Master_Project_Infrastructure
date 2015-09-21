# Master_Project_Infrastructure

This project is to construct all of the infrastructure of the Master Project of Snaplogic Monitor System.

# DESRIPTIOIN #

- Use docker to depoly the zookeeper and kafka cluster.
- Use the maestro-ng tool to manage all of service in the cluster.

# REQUIREMENTS #

- All of the nodes in the cluster have to run a docker daemon on it.
- The host computer have to install the maestro-ng.

# USAGE #

- Change the maestro.yaml file to configure your cluster information.
- Run maestro by this yaml file.
