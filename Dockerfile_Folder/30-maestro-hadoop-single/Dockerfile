FROM 20-maestro-hadoop
MAINTAINER Wentao Du <vdu@snaplogic.com>

RUN apt-get -y install sshpass
ADD 20-sendKey.sh  /opt/setup/scripts/
ADD 30-start-hadoop.sh  /opt/setup/scripts/

ADD core-site.xml /usr/local/hadoop/etc/hadoop/core-site.xml 
ADD hdfs-site.xml /usr/local/hadoop/etc/hadoop/hdfs-site.xml
ADD mapred-site.xml /usr/local/hadoop/etc/hadoop/mapred-site.xml
ADD yarn-site.xml /usr/local/hadoop/etc/hadoop/yarn-site.xml
