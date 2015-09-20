#Dockerfile for Kafka

FROM 10-maestro_base

RUN apt-get -y install netcat-traditional netcat-openbsd nmap
RUN pip install kazoo && apt-get clean iputils-ping

# Install zookeeper
RUN wget -q -O - http://mirrors.sonic.net/apache/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz  | tar -C /opt -xz

ADD run-zookeeper.py /opt/zookeeper-3.4.6/.docker/            
RUN mkdir -p /var/docker-share

WORKDIR /opt/zookeeper-3.4.6/.docker/
VOLUME /var/docker-share
CMD ["python", "run-zookeeper.py"]
