#!/bin/bash

docker -H tcp://192.168.0.107:2375 exec -it kafka-dc-3 /opt/kafka/bin/kafka-console-producer.sh --broker-list 192.168.0.107:9092 --topic test1
