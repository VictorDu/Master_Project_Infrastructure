#Dockerfile for Kafka

FROM 10-maestro_base

RUN apt-get -y update
RUN apt-get -y install maven
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer
RUN  apt-get -y install git python-setuptools
RUN apt-get -y install git python-setuptools
ADD build-run-kafka-consumer.sh /opt/
WORKDIR /opt

CMD ["bash", "build-run-kafka-consumer.sh"]
