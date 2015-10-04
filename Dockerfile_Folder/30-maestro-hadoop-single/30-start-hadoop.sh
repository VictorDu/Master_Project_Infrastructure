#!/bin/bash

mkdir -p /usr/local/hadoop_tmp/hdfs/datanode
mkdir -p /usr/local/hadoop_tmp/hdfs/namenode

cd /usr/local/hadoop
bin/hdfs namenode -format
sbin/start-dfs.sh
sbin/start-yarn.sh

