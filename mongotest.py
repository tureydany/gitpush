import pymongo


client = pymongo.MongoClient("mongodb+srv://turey_dany:arul2304@cluster0.egy97.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

#client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
#db = client.test
#print(db)
d={
    "name":"tuery",
    "surname":"dany",
    "email":"tureydany19@gmail.com"
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)