#!/bin/bash

docker -H tcp://192.168.0.106:2375 exec -it Master cat /etc/hosts
docker -H tcp://192.168.0.105:2375 exec -it slave-dc-2 cat /etc/hosts
docker -H tcp://192.168.0.107:2375 exec -it slave-dc-3 cat /etc/hosts
