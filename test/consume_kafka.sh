#!/bin/bash
echo Check kafka3
docker -H tcp://192.168.0.107:2375 exec -it kafka-dc-3 /opt/kafka/bin/kafka-topics.sh --describe --zookeeper 192.168.0.107:2181 --topic test1
echo Check kafka2
docker -H tcp://192.168.0.105:2375 exec -it kafka-dc-2 /opt/kafka/bin/kafka-topics.sh --describe --zookeeper 192.168.0.105:2181 --topic test1
echo Check kafka1
docker -H tcp://192.168.0.106:2375 exec -it kafka-dc-1 /opt/kafka/bin/kafka-topics.sh --describe --zookeeper 192.168.0.106:2181 --topic test1


