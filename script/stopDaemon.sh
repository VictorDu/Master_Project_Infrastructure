#!/bin/bash

password=$1

#array=(1 2 3 2 1)
nodesi_ip=("192.168.0.105" "192.168.0.106" "192.168.0.107")
for ip in ${nodes_ip[@]}
do
  sshpass -p password ssh $ip -l root "killall docker"
done
