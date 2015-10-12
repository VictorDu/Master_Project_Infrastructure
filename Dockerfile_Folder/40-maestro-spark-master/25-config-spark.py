#!/usr/bin/env python

import os
import sys
import subprocess
import shutil
from jinja2 import Environment

from maestro.guestutils import get_container_name, \
    get_container_host_address, \
    get_environment_name, \
    get_node_list, \
    get_port, \
    get_service_name, \
    get_specific_host, \
    get_specific_port, \
    _get_service_instance_names

servers = _get_service_instance_names('hadoop-slave')
dict={}
for server in servers:
    host = get_specific_host('hadoop-slave', server)
    dict[host] = server

slaves = """{% for key, value in _dict.iteritems() %}echo "{{ value }}" >> /usr/local/spark/spark-1.5.1-bin-hadoop2.6/conf/slaves
{% endfor %}{% for key, value in _dict.iteritems() %}sshpass -p '123' ssh {{ key }} -l root "mkdir -p /usr/local/spark"
scp -r /usr/local/spark/spark-1.5.1-bin-hadoop2.6 root@{{ key }}:/usr/local/spark
{% endfor %}"""

with open("shells.sh", "wb") as f:
    f.write(Environment().from_string(slaves).render(_dict=dict))
subprocess.call(["bash", "shells.sh"])
