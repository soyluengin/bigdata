import matplotlib.pyplot as plt
import pymongo
def getDb():
        client = pymongo.MongoClient("mongodb://192.168.1.35:27017/")
        db = client["crypto"]
        return db

db = getDb()
coll = db["userAsset"]
assets=coll.find().sort("change_24h")

mostValuableAsset = assets[0]
print(mostValuableAsset['asset_Id'])
print(mostValuableAsset['change_24h'])


assetColl = db["asset"]
assets2=assetColl.find({"asset_id": mostValuableAsset['asset_Id']}).sort("updated_at")

assetTime = []
assetValues = []
counter = 0
minDate = assets2[0]['updated_at']
maxDate = assets2[assets2.count() -1]['updated_at']
for asset1 in assets2:
   # print(asset1)
    assetTime.append(counter)
    counter = counter + 1 
    assetValues.append(asset1['price'])
 


# plotting the points
plt.plot(assetTime, assetValues)
 
# naming the x axis
plt.xlabel('Time ' + minDate + " - " + maxDate)
# naming the y axis
plt.ylabel('Price')
 
# giving a title to my graph
plt.title( mostValuableAsset['asset_Id'] + " / USD")
 
# function to show the plot
plt.show()