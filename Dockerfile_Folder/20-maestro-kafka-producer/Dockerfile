#Dockerfile for Kafka

FROM 10-maestro_base

RUN apt-get -y update
RUN  apt-get -y install maven git python-setuptools
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer
ADD build-run-kafka-producer.sh /opt/
WORKDIR /opt

CMD ["bash", "build-run-kafka-producer.sh"]
