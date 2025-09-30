from pymongo import MongoClient

mongo_uri = "mongodb+srv://<username:pw>@cluster0.egseduj.mongodb.net/"
conn = MongoClient(mongo_uri)
db = conn["<db name>"]
