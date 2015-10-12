#!/bin/bash

nodes_ip=("192.168.0.105" "192.168.0.107")
for node in ${nodes_ip[@]}
do
  echo "start rsync to $node"
  rsync -r /root/WentaoDu/Master_Project/Master_Project_Infrastructure root@$node:/root
  rsync -r /root/docker-share root@192.168.0.105:/root
  echo "finish rsync to $node"
done
