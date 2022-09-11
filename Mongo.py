import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:ineuron@cluster0.bgcr20g.mongodb.net/?retryWrites=true&w=majority")
db = client.test
data ={
    'name':"abhy",
    "mailId":"aky@gmail.com",
    "subject":["Datascience","big data","data analytics"]
}
database = client['inventory5']
collection = database['data']
db.getCollection("test").ensureIndex ({"a" : 1}, {unique: true})
#collection.insert_one(data)
dbs = client.list_database_names()
my_col = database.list_collection_names()
db_test = dbs[0]
print(my_col)