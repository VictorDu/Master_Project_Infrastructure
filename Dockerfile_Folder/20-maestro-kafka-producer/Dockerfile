#Dockerfile for Kafka

FROM 10-maestro_base

RUN apt-get -y update
RUN apt-get -y install git python-setuptools
RUN easy_install pip
RUN pip install kafka-python

CMD ["bash", "build-run-kafka-producer.sh"]
