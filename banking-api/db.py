from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["bankdb"]

users_collection = db["users"]
accounts_collection = db["accounts"]
transaction_collection = db["transactions"]


accounts_collection.create_index("userId")
transaction_collection.create_index("accountId")
transaction_collection.create_index("createdAt")

