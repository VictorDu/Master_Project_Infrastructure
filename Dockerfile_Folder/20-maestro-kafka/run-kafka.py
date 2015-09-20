#!/usr/bin/env python

# Copyright (C) 2013 SignalFuse, Inc.

# Start script for the Kafka service.
# Requires kazoo, a pure-Python ZooKeeper client.

from kazoo.client import KazooClient
import logging
import os
import sys

from maestro.guestutils import get_container_name, \
    get_container_host_address, \
    get_environment_name, \
    get_node_list, \
    get_port, \
    get_service_name, \
    get_specific_host, \
    get_specific_port

# Setup logging for Kazoo.
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

os.chdir(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..'))

def getKafkaZookeeperNode(name):
    return '{}:{}'.format(
        get_specific_host('zookeeper', name),
        get_specific_port('zookeeper', name, 'client'))
    
def getKafkaZookeeper():
    servers = os.environ['ZOOKEEPER_SERVER_IDS'].split(',')
    return ','.join(map(getKafkaZookeeperNode, servers))

KAFKA_CONFIG_FILE = os.path.join('config', 'server.properties')
KAFKA_LOGGING_CONFIG = os.path.join('config', 'log4j.properties')
ZOOKEEPER_NODE_LIST = getKafkaZookeeper()
sys.stderr.write(ZOOKEEPER_NODE_LIST)
HOST_IP = get_container_host_address()
LOG_PATTERN = "%d{yyyy'-'MM'-'dd'T'HH:mm:ss.SSSXXX} %-5p [%-35.35t] [%-36.36c]: %m%n"

KAFKA_CONFIG_TEMPLATE = """# Kafka configuration for %(node_name)s
broker.id=%(broker_id)d
port=%(broker_port)d

log.dirs=%(log_dirs)s
num.partitions=%(num_partitions)d

zookeeper.connect=%(zookeeper_connect)s
zookeeper.connection.timeout.ms=6000
zookeeper.session.timeout.ms=6000
zookeeper.sync.time.ms=2000

advertised.host.name=%(host_ip)s
"""

KAFKA_LOGGING_TEMPLATE = """# Log4j configuration, logs to rotating file
log4j.rootLogger=INFO,R

log4j.appender.R=org.apache.log4j.RollingFileAppender
log4j.appender.R.File=/var/log/%(service_name)s/%(container_name)s.log
log4j.appender.R.MaxFileSize=100MB
log4j.appender.R.MaxBackupIndex=10
log4j.appender.R.layout=org.apache.log4j.PatternLayout
log4j.appender.R.layout.ConversionPattern=%(log_pattern)s
"""

# Generate the Kafka configuration from the defined environment variables.
config_model = {
    'node_name': get_container_name(),
    'broker_id': int(os.environ.get('BROKER_ID', 0)),
    'broker_port': get_port('broker'),
    # Default log directory is /var/lib/kafka/logs.
    'log_dirs': os.environ.get('LOG_DIRS', '/var/lib/kafka/logs'),
    'zookeeper_connect': ZOOKEEPER_NODE_LIST,
    'num_partitions': int(os.environ.get('NUM_PARTITIONS',1)),
    'host_ip': HOST_IP
}

with open(KAFKA_CONFIG_FILE, 'w+') as conf:
    conf.write(KAFKA_CONFIG_TEMPLATE % config_model)


# Setup the logging configuration.
logging_model = {
    'service_name': 'ZOOKEEPER',
    'container_name': get_container_name(),
    'log_pattern': LOG_PATTERN
}
with open(KAFKA_LOGGING_CONFIG, 'w+') as f:
    f.write(KAFKA_LOGGING_TEMPLATE % logging_model)

KAFKA_ZOOKEEPER_BASE = os.environ.get('ZOOKEEPER_DATADIR', '/tmp/zookeeper')
#ZOOKEEPER_NODE_LIST = os.environ.get('ZOOKEEPER_CONNECT', 'localhost:2181')
def ensure_kafka_zk_path(retries=1):
    while retries >= 0:
        # Connect to the ZooKeeper nodes. Use a pretty large timeout in case they were
        # just started. We should wait for them for a little while.
    #    sys.stderr.write(ZOOKEEPER_NODE_LIST)
        zk = KazooClient(hosts=ZOOKEEPER_NODE_LIST, timeout=30000)
        try:
            zk.start()
            zk.ensure_path(KAFKA_ZOOKEEPER_BASE)
            return True
        except:
            retries -= 1
        finally:
            zk.stop()
    return False

if not ensure_kafka_zk_path(retries = int(os.environ.get('NODE_NUMBER',1))):
    sys.stderr.write('Could not create the base ZooKeeper path for Kafka!\n')
    sys.exit(1)

# Start the Kafka broker.
os.execl('bin/kafka-server-start.sh', 'kafka', 'config/server.properties')
