#!/bin/bash

newPassword="123"
expect -c "
        spawn passwd
        expect "?assword:"
        send \"$newPassword\r\"
        expect "?assword:"
        send \"$newPassword\r\"
        expect eof"
sed -i -e s/without-password/yes/g /etc/ssh/sshd_config
service ssh restart
