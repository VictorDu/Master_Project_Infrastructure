#!/usr/bin/env python

import os
import sys
import subprocess
import shutil
from jinja2 import Environment


#shutil.rmtree('/usr/local/hadoop_tmp/')
#shutil.rmtree('/usr/local/hadoop/tmp/')
#servers = _get_service_instance_names('hadoop-slave')
dict={"192.169.0.105":"Slave1", "192.168.0.107":"Slave2"}

slaves = """{% for key, value in _dict.iteritems() %}{{ key }}
{% endfor %}"""
slaves_file= Environment().from_string(slaves).render(_dict=dict)
with open("slaves", "wb") as f:
    f.write(slaves_file)
with open("masters", "wb") as f:
    f.write("Master\n")

#host = get_specific_port('spark-master', 'Master')
host="192.168.0.106"
dict[host] = 'Master'
shell_single = """rsync -avxP /usr/local/hadoop/ root@{{ hostname }}:/usr/local/hadoop/
{% for key, value in _dict.iteritems() %}sshpass -p '123' ssh {{ key }} -l root "echo \\"{{ key }}     {{ value }}\\" >> /etc/hosts"
{% endfor %}"""
def write_single(ip, dict):
    temp = dict.copy()
    del temp[ip]
    return Environment().from_string(shell_single).render(_dict=temp, hostname=dict[ip])

shell = """#!/bin/bash
{% for single in single_shells %}{{ single }}{% endfor %}"""
single_shells = map(lambda (x,y): write_single(x, dict), dict.items())
with open("shells-result.sh", "wb") as f:
    f.write(Environment().from_string(shell).render(single_shells=single_shells))
#subprocess.call(["bash", "shells.sh"])
