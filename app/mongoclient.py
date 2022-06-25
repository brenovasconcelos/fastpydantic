from pymongo_inmemory import MongoClient
from app.helpers import generate_random_data_test


class MongoSteeleye:
    def __init__(self) -> None:

        self.client = self.start_client()
        self.db = self.client["steeleye"]
        self.collection = self.db["trades"]

        self.load_db()
    
    def make_query(self, query={}):

        ret = self.collection.find(query, projection={"_id": False})
        return list(ret)

    def load_db(self):
        data_test = generate_random_data_test()
        loaded = self.collection.insert_many(data_test)
        return loaded

    def start_client(self):
        client = MongoClient()

        return client

    def teardown(self):
        self.client.close()