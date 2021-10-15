import matplotlib.pyplot as plt
import pymongo
def getDb():
        client = pymongo.MongoClient("mongodb://192.168.1.35:27017/")
        db = client["crypto"]
        return db

db = getDb()
coll = db["userAsset"]
userAssets=coll.find({"balance":{"$gt":0}})

minDate = '2021-10-11T18:16:38.465730'
assetColl = db["asset"]

for userAsset in userAssets:
    assets=assetColl.find({"asset_id": userAsset['asset_Id'],"updated_at": {"$gte":minDate}}).sort("updated_at")
    assetTime = []
    assetValues = []
    counter = 0

    for asset in assets:
        assetTime.append(counter)
        counter = counter + 1 
        assetValues.append(asset['price']*userAsset['balance'])
    
    plt.plot(assetTime, assetValues, label = userAsset['asset_Id'])

 
 
# naming the x axis
plt.xlabel('time')
# naming the y axis
plt.ylabel('Balance')
# giving a title to my graph
plt.title('Total Balance Graph!')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()