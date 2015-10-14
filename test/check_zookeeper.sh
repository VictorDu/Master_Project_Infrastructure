#!/bin/bash

docker -H tcp://192.168.0.106:2375 exec -it zookeeper-dc-1 /opt/zookeeper-3.4.6/bin/zkServer.sh status
docker -H tcp://192.168.0.105:2375 exec -it zookeeper-dc-2 /opt/zookeeper-3.4.6/bin/zkServer.sh status
docker -H tcp://192.168.0.107:2375 exec -it zookeeper-dc-3 /opt/zookeeper-3.4.6/bin/zkServer.sh status
