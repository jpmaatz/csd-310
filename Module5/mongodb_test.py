import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ivbia.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
print()
print("-- Pytech C0llection List --")
print(db.list_collection_names())
print()
input ("End of program, press any key to exit...")