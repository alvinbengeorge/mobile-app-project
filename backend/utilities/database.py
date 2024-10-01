from pymongo import MongoClient

import os

class Database:
    def __init__(self):
        uri = os.getenv("MONGO_URI") or "mongodb://localhost:27017"
        self.client = MongoClient(uri)
        self.db = self.client["food"]
        