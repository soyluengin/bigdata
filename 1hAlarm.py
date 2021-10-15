import sys
import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import pyspark.sql.functions as f
from pyspark.sql.types import StructType, StructField, StringType, ArrayType
import pymongo

def insertDb(x):
        print(x)
        mydb = getDb()
        mycol = mydb["alarm1h"]
        doc1={
"asset_id":x["ASSET_ID"],
"name":x["NAME"],
"price":x["PRICE"],
"change1h":x["CHANGE_1H"],
"updated_at":x["UPDATED_AT"]
}
        mycol.insert_one(doc1)

def getDb():
        client = pymongo.MongoClient("mongodb://192.168.1.35:27017/")
        db = client["alarm1h"]
        return db

def write_last1h(df, epoch_id):
    print("Fiyat değişimi son 1 saat içinde %2 oranında düşen varlıklar bilgisi")
    df.foreach(insertDb)

if __name__ == "__main__":

    spark = SparkSession\
        .builder\
        .appName("AssetSparkSession")\
        .getOrCreate()
    bootstrapServers = "192.168.1.35:9092"
    subscribeType = "subscribe"
    topics = "assetEvents"

    assetSchema = StructType([
        StructField("assets",ArrayType(
                StructType([
                        StructField("asset_id", StringType()),
                        StructField("name", StringType()),
                        StructField("price", DoubleType()),
                        StructField("volume_24h", DoubleType()),
                        StructField("change_1h", DoubleType()),
                        StructField("change_24h", DoubleType()),
                        StructField("change_7d", DoubleType()),
                        StructField("status", StringType()),
                        StructField("created_at", StringType()),
                        StructField("updated_at", StringType())
                ])
        ),True)
    ])

    allAssets = spark\
        .readStream\
        .format("kafka")\
        .option("kafka.bootstrap.servers", bootstrapServers)\
        .option(subscribeType, topics)\
        .load()

    assets = allAssets\
        .select(from_json(col("value").cast("string"), assetSchema).alias("value")) \

    assets = assets.selectExpr("explode(value.assets) as asset")

    assets = assets\
        .withColumn("ASSET_ID", expr("asset.asset_id"))\
        .withColumn("NAME", expr("asset.name"))\
        .withColumn("PRICE", expr("asset.price"))\
        .withColumn("VOLUME_24H", expr("asset.volume_24h"))\
        .withColumn("CHANGE_1H", expr("asset.change_1h"))\
        .withColumn("CHANGE_24H", expr("asset.change_24h"))\
        .withColumn("CHANGE_7D", expr("asset.change_7d"))\
        .withColumn("UPDATED_AT", expr("asset.updated_at"))\
        .drop("asset")

    assets1h = assets\
        .where("asset.change_1h < -2 ")
    q1 = assets1h.writeStream.foreachBatch(write_last1h).start()
#    query2 = assets1h\
#        .writeStream\
#        .outputMode("append")\
#        .format("console")\
#        .start()
    q1.awaitTermination()

