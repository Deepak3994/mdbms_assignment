from pymongo import MongoClient
import pymongo

client = MongoClient()
#which database to connect
db = client.TB
contents = db.collection_name.find({"country":"India"})
#printing the contents of the database
for document in contents:
	print(document)