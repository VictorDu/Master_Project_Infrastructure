#!/bin/bash

cd /usr/local/hadoop
bin/hdfs namenode -format
sbin/start-dfs.sh
sbin/start-yarn.sh

#sbin/hadoop-daemon.sh start namenode
#sbin/hadoop-daemon.sh start datanode
#sbin/yarn-daemon.sh start resourcemanager
#sbin/yarn-daemon.sh start nodemanager
sbin/mr-jobhistory-daemon.sh start historyserver

jps
