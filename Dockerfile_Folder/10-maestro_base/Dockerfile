# Dockerfile for Maestro Base

FROM ubuntu:15.04
MAINTAINER Wentao Du <vdu@snaplogic.com>

# Install the basic application
RUN echo /etc/issue
RUN apt-get -y update
RUN apt-get -y install vim git tar unzip wget python-setuptools

# Install maestro ng lib
RUN apt-get -y install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev
RUN easy_install pip
RUN pip install pyyaml
RUN pip install --upgrade requests
RUN pip install docker-py
RUN pip install Jinja2
RUN pip install --user --upgrade git+git://github.com/signalfuse/maestro-ng

# Install the basic Java
RUN apt-get -y install default-jre default-jdk
RUN apt-get -y update
