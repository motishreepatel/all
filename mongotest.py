import pymongo
client = pymongo.MongoClient("mongodb+srv://Motishree:Namish123@motishreecluster.5vopd.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {

    "name":"sudhnshu",
    "email": "s@ineuron.ai",
    "surname": "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)