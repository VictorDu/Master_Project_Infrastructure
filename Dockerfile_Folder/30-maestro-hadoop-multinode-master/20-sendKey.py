#!/usr/bin/env python

import os
import sys
import time
import subprocess
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
servers_ip = map(lambda name: get_specific_host('hadoop-slave', name), servers)

time.sleep(30)
sendkeybash = """#!/bin/bash
{% for slave_ip in slave_ips %}expect -c "
        spawn "scp\\ /root/.ssh/id_rsa.pub\\ root@{{ slave_ip }}:/root"
        expect "?assword:"
        send \\\"{{ password }}\\r\\\"
        expect eof"
sshpass -p '{{ password }}' ssh {{ slave_ip }} -l root "cat ~/id_rsa.pub >> ~/.ssh/authorized_keys"
{% endfor %}"""
fileContent = Environment().from_string(sendkeybash).render(password="123", slave_ips=servers_ip)
with open("sendKey.sh", "wb") as f:
    f.write(fileContent)
subprocess.call(["bash", "sendKey.sh"])
