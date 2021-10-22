# Crypto analysis
![diagram](https://user-images.githubusercontent.com/32875227/137445868-b1372158-71f4-4eed-966c-06d8c7c0bfa3.jpg)

# G1 - Anlık portföy değer bilgisi
![image](https://user-images.githubusercontent.com/32875227/138423572-fe45a856-8904-4a05-8c8c-7f6ef2f1b2fd.png)

# G2 - Portföydeki son 24 saat içerisinde en çok artış gösteren varlığın zaman/fiyat grafiği
![image](https://user-images.githubusercontent.com/32875227/138424291-840c4bf1-33c3-4822-85b4-651269a3393d.png)

# G3 - Portföydeki son 24 saat içerisinde en çok kayıp gösteren varlığın zaman/fiyat grafiği
![image](https://user-images.githubusercontent.com/32875227/138424454-2e79291d-86a7-4ce0-90c3-84b475bb9da5.png)

# G4 - Portföydeki tüm varlıkların USD toplamının son 24 saat içerisindeki zaman/fiyat grafiği
![image](https://user-images.githubusercontent.com/32875227/138423717-5f3cf8d4-db60-4f82-b27b-ad411f28069a.png)

# MongoDb

![image](https://user-images.githubusercontent.com/32875227/138425183-0279a9d2-3386-4936-a6e4-930b26d29ec5.png)

# start zookeeper and kafka
sudo /home/ubuntu/kafka/bin/zookeeper-server-start.sh config/zookeeper.properties 
sudo /home/ubuntu/kafka/bin/kafka-server-start.sh /home/ubuntu/kafka/config/server.properties

# kafka producer test
python3 /home/ubuntu/BigData/kafkaProducer.py

# 24 saatlik alarm
/opt/spark/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.0.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 24hAlarm.py

# 1 saatlik alarm
/opt/spark/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.0.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 1hAlarm.py
