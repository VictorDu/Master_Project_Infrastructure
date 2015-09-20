#Dockerfile for Kafka

FROM 10-maestro_base

RUN apt-get -y install netcat-traditional netcat-openbsd nmap
RUN pip install kazoo && apt-get clean iputils-ping


RUN wget http://www.webhostingjams.com/mirror/apache//kafka/0.8.2.0/kafka_2.10-0.8.2.0.tgz
RUN tar -xzf kafka_2.10-0.8.2.0.tgz
RUN mv kafka_2.10-0.8.2.0 /opt/kafka    

ADD run-kafka.py /opt/kafka/.docker/
WORKDIR /opt/kafka/.docker/
CMD ["python", "run-kafka.py"]
