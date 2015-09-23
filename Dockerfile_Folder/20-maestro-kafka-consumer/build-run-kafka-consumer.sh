#!/bin/bash

git clone https://github.com/kaijiezhou/Kafka-JavaDemo.git
cd Kafka-JavaDemo
mvn clean
mvn install
cd target
java -jar demo-0.0.1-SNAPSHOT-jar-with-dependencies.jar consumer $ZOOKEEPER_INFO
