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

slaves = """{% for key, value in _dict.iteritems() %}echo {{ value }} >> /usr/local/hadoop/etc/hadoop/slaves
{% endfor %}"""
slaves_file= Environment().from_string(slaves).render(_dict=dict)
#f = open("/usr/local/hadoop/etc/hadoop/slaves", "wb")
#f.write(slaves_file)
#f.close()
#f = open("/usr/local/hadoop/etc/hadoop/masters", "wb")
#f.write("Master\n")
#f.close()

host = get_specific_host('spark-master', 'Master')
dict[host] = 'Master'
shell_single = """scp -r /usr/local/hadoop root@{{ _ip }}:/usr/local
{% for key, value in _dict.iteritems() %}sshpass -p '123' ssh {{ _ip }} -l root "echo \"{{ key }}     {{ value }}\" >> /etc/hosts"
{% endfor %}"""
def write_single(ip, dict):
    temp = dict.copy()
    del temp[ip]
    return Environment().from_string(shell_single).render(_dict=temp, _ip=ip)

shell = """#!/bin/bash
rm -rf /usr/local/hadoop/etc/hadoop/slaves
{{ _slave_files }}
echo Master >> /usr/local/hadoop/etc/hadoop/masters
{% for single in single_shells %}{{ single }}{% endfor %}"""

single_shells = map(lambda (key, value): write_single(key, dict), dict.items())
with open("shells.sh", "wb") as f:
    f.write(Environment().from_string(shell).render(single_shells=single_shells, _slave_files=slaves_file))
f.close()

subprocess.call(["cat", "shells.sh"])
subprocess.call(["bash", "shells.sh"])
