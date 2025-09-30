from pymongo import MongoClient

mongo_uri = "mongodb+srv://prakirtibista7:Bunuchhetry2@cluster0.egseduj.mongodb.net/"
conn = MongoClient(mongo_uri)
db = conn["notes"]