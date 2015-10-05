#!/bin/bash

echo "192.168.0.105     Slave" >> /etc/hosts
mkdir -p /usr/local/hadoop_tmp/hdfs/datanode
mkdir -p /usr/local/hadoop_tmp/hdfs/namenode
rm -rf /usr/local/hadoop_tmp/
rm -rf /usr/local/hadoop/tmp/

rsync -avxP /usr/local/hadoop/ root@Slave:/usr/local/hadoop/
sshpass -p '123' ssh 192.168.0.105 -l root "rm -rf /usr/local/hadoop/tmp/"
sshpass -p '123' ssh 192.168.0.105 -l root "echo \"192.168.0.106     Master\" >> /etc/hosts"

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
