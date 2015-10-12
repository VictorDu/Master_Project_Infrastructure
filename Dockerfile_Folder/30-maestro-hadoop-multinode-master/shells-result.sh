#!/bin/bash
rsync -avxP /usr/local/hadoop/ root@Slave1:/usr/local/hadoop/
sshpass -p '123' ssh 192.168.0.107 -l root "echo \"192.168.0.107     Slave2\" >> /etc/hosts"
sshpass -p '123' ssh 192.168.0.106 -l root "echo \"192.168.0.106     Master\" >> /etc/hosts"
rsync -avxP /usr/local/hadoop/ root@Slave2:/usr/local/hadoop/
sshpass -p '123' ssh 192.169.0.105 -l root "echo \"192.169.0.105     Slave1\" >> /etc/hosts"
sshpass -p '123' ssh 192.168.0.106 -l root "echo \"192.168.0.106     Master\" >> /etc/hosts"
rsync -avxP /usr/local/hadoop/ root@Master:/usr/local/hadoop/
sshpass -p '123' ssh 192.169.0.105 -l root "echo \"192.169.0.105     Slave1\" >> /etc/hosts"
sshpass -p '123' ssh 192.168.0.107 -l root "echo \"192.168.0.107     Slave2\" >> /etc/hosts"
