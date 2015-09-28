rm /usr/local/hadoop/etc/hadoop/slaves
echo $SLAVE_IP >> /usr/local/hadoop/etc/hadoop/slaves

sed -i -e s/Master/192.168.0.106/g  /usr/local/hadoop/etc/hadoop/core-site.xml
cd /usr/local
tar -zcf ./hadoop.tar.gz ./hadoop-2.6.0
scp hadoop.tar.gz root@$SLAVE_IP:/root

sshpass -p '123' ssh $SLAVE_IP -l root "tar -zxf /root/hadoop.tar.gz -C /usr/local"
