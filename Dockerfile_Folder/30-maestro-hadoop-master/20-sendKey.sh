#!/bin/bash

newPassword="123"
expect -c "
        spawn "scp\ /root/.ssh/id_rsa.pub\ root@$SLAVE_IP:/root"
        expect "?assword:"
        send \"$newPassword\r\"
        expect eof"
sshpass -p '123' ssh 192.168.0.105 -l root "cat ~/id_rsa.pub >> ~/.ssh/authorized_keys"
