#!/usr/bin/env python

# Copyright (C) 2013 SignalFuse, Inc.

# Start script for the Kafka service.
# Requires kazoo, a pure-Python ZooKeeper client.

import logging
import os
import sys
import time 

from maestro.guestutils import (
    get_container_name, get_node_list, get_service_name, get_port,
    get_specific_host, get_specific_port, get_container_host_address,
    get_environment_name)

sys.stderr.write('zookeeper start')
    
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
ZOOKEEPER_CONFIG_FILE = os.path.join('conf', 'zoo.cfg')
ZOOKEEPER_LOG_CONFIG_FILE = os.path.join('conf', 'log4j.properties')
LOG_PATTERN = ("%d{yyyy'-'MM'-'dd'T'HH:mm:ss.SSSXXX} %-5p [%-35.35t] [%-36.36c]:%m%n")

conf = {
        'tickTime': int(os.environ.get('ZOOKEEPER_TICKTIME', 10)),
	'initLimit': 10,
        'syncLimit': 5,
        'dataDir': os.environ.get('ZOOKEEPER_DATADIR', '/tmp/zookeeper'),
        'clientPort': os.environ.get('ZOOKEEPER_CLIENTPORT', 2181),
	'quorumListenOnAllIPs': True,
        'autopurge.snapRetainCount': int(os.environ.get('MAX_SNAPSHOT_RETAIN_COUNT', 10)),
        'autopurge.purgeInterval': int(os.environ.get('PURGE_INTERVAL', 24))
}

with open(ZOOKEEPER_CONFIG_FILE, 'w+') as f:
    for entry in conf.iteritems():
        f.write("%s=%s\n" % entry)

def build_node_repr(name):
    """Build the representation of a node with peer and leader-election
    ports."""
    return '{}:{}:{}'.format(
        get_specific_host(get_service_name(), name),
        get_specific_port(get_service_name(), name, 'peer'),
        get_specific_port(get_service_name(), name, 'leader_election'))

if os.environ.get('ZOOKEEPER_SERVER_IDS'):
    servers = os.environ['ZOOKEEPER_SERVER_IDS'].split(',')
    for server in servers:
        node, id = server.split(':')
        newline = 'server.{}={}'.format(id, build_node_repr(node))
        with open( ZOOKEEPER_CONFIG_FILE , "a") as myfile:
            myfile.write(newline)
            myfile.write("\n")
#        conf['server.{}'.format(id)] = build_node_repr(node)
        if node == get_container_name():
            ZOOKEEPER_NODE_ID = id
os.mkdir(os.environ.get('ZOOKEEPER_DATADIR'))

with open(os.path.join(os.environ.get('ZOOKEEPER_DATADIR'), 'myid'), 'w+') as f:
        f.write('%s\n' % ZOOKEEPER_NODE_ID)

with open (ZOOKEEPER_CONFIG_FILE, "r") as myfile:
    data=myfile.read()
    sys.stderr.write(data)

with open(ZOOKEEPER_LOG_CONFIG_FILE, 'w+') as f:
    f.write("""# Log4j configuration, logs to rotating file
log4j.rootLogger=INFO,R
log4j.appender.R=org.apache.log4j.RollingFileAppender
log4j.appender.R.File=/var/log/%s/%s.log
log4j.appender.R.MaxFileSize=100MB
log4j.appender.R.MaxBackupIndex=10
log4j.appender.R.layout=org.apache.log4j.PatternLayout
log4j.appender.R.layout.ConversionPattern=%s
""" % (get_service_name(), get_container_name(),LOG_PATTERN))

#os.execl('bin/zkServer.sh', 'zookeeper', 'start-foreground')
os.execl('bin/zkServer.sh', 'zookeeper' ,'start-foreground')
sys.stderr.write('zookeeper over')
while True:
    time.sleep(60)

sys.stderr.write('zookeeper over')
