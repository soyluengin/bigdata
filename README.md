# Crypto analysis
![diagram](https://user-images.githubusercontent.com/32875227/137445868-b1372158-71f4-4eed-966c-06d8c7c0bfa3.jpg)



# start zookeeper and kafka
sudo /home/ubuntu/kafka/bin/zookeeper-server-start.sh config/zookeeper.properties 
sudo /home/ubuntu/kafka/bin/kafka-server-start.sh /home/ubuntu/kafka/config/server.properties

# kafka producer test
python3 /home/ubuntu/BigData/kafkaProducer.py

# 24 saatlik alarm
/opt/spark/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.0.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 24hAlarm.py

# 1 saatlik alarm
/opt/spark/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.0.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 1hAlarm.py
