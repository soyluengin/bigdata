import matplotlib.pyplot as plt
import pymongo
def getDb():
        client = pymongo.MongoClient("mongodb://192.168.1.35:27017/")
        db = client["crypto"]
        return db

db = getDb()
coll = db["userAsset"]
assets=coll.find()

assetNames = []
assetValues = []
for asset in assets:
    assetNames.append(asset['asset_Id'])
    assetValues.append(asset['balance']*asset['current_Value'])
    

# plotting the pie chart
plt.pie(assetValues, labels = assetNames, colors=None,
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
        radius = 1.2, autopct = '%1.1f%%')
 
# plotting legend
plt.legend()
 
# showing the plot
plt.show()