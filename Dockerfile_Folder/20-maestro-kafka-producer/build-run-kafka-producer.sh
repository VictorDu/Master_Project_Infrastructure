#!/bin/bash

git clone https://github.com/kaijiezhou/Kafka-JavaDemo.git
cd Kafka-JavaDemo
mvn clean
mvn install
cd target
while true
do
   sleep 1
   java -jar demo-0.0.1-SNAPSHOT-jar-with-dependencies.jar producer $KAFKA_INFO generater 5 
done
