import pymongo
def getDb():
        client = pymongo.MongoClient("mongodb://192.168.1.35:27017/")
        db = client["crypto"]
        return db

db = getDb()
coll = db["userAsset"]
userAssets=coll.find({"balance":{"$gt":0}},{"asset_id":"BTC"})

minDate = '2021-10-08T09:16:38.465730'
assetColl = db["asset"]
lossAsset = ''
lossRate = 0
lossRateTime = 0
previousPrice = 0

for userAsset in userAssets:
    assets=assetColl.find({"asset_id": userAsset['asset_id'],"updated_at": {"$gte":minDate}}).sort("updated_at")
    #assets=assetColl.find({"asset_id": 'XRP',"updated_at": {"$gte":minDate}}).sort("updated_at")
    for asset in assets:
        if(previousPrice>0):
            rate = (previousPrice - asset['price']) / previousPrice;
           # print('price: ' + str(asset['price']))
           # print('rate: ' + str(rate))
            if(rate > lossRate):
                lossRate=rate
                lossRateTime =asset['updated_at'] 
                lossAsset = asset['asset_id']
           #     print('lossRate : ' + str(lossRate))
        else:
            previousPrice=asset['price']
            
print('lossRate : ' + str(lossRate))
print('lossRateTime : ' + str(lossRateTime))
print('lossAsset : ' + str(lossAsset))          