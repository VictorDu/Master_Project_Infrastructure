#!/bin/bash

echo "Slave" >> /usr/local/spark/spark-1.5.1-bin-hadoop2.6/conf/slaves
sshpass -p '123' ssh 192.168.0.105 -l root "mkdir -p /usr/local/spark"
scp -r /usr/local/spark/spark-1.5.1-bin-hadoop2.6 root@192.168.0.105:/usr/local/spark
