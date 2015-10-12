#Dockerfile for Kafka

FROM 30-maestro-hadoop-multinode-master

RUN wget http://www.scala-lang.org/files/archive/scala-2.10.4.tgz
RUN mkdir -p /usr/local/src/scala
RUN tar -zxvf scala-2.10.4.tgz -C /usr/local/src/scala/
RUN echo "export SCALA_HOME=/usr/local/src/scala/scala-2.10.4" >> ~/.bashrc1
RUN echo "export PATH=\$SCALA_HOME/bin:\$PATH" >> ~/.bashrc1
RUN cat ~/.bashrc1
RUN sh ~/.bashrc1

RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-1.5.1-bin-hadoop2.6.tgz
RUN mkdir -p /usr/local/spark
RUN tar -zxvf spark-1.5.1-bin-hadoop2.6.tgz -C /usr/local/spark/
ADD spark-env-addition.sh /var/
RUN cp /usr/local/spark/spark-1.5.1-bin-hadoop2.6/conf/spark-env.sh.template /usr/local/spark/spark-1.5.1-bin-hadoop2.6/conf/spark-env.sh
RUN cat /var/spark-env-addition.sh >> /usr/local/spark/spark-1.5.1-bin-hadoop2.6/conf/spark-env.sh
#ADD 25-config-spark.sh /opt/setup/scripts/
ADD 25-config-spark.py /opt/setup/scripts/
ADD 35-start-spark.sh /opt/setup/scripts/
