from typing import Dict, List

from pymongo_inmemory import MongoClient

from app.helpers import generate_random_data_test


class MongoSteeleye:
    def __init__(self) -> None:

        self.client = self.start_client()
        self.db = self.client["steeleye"]
        self.collection = self.db["trades"]

        self.load_db()

    def make_query(
        self,
        search: str = None,
        asset_class: str = None,
        end: str = None,
        max_price: str = None,
        min_price: str = None,
        start: str = None,
        trade_type: str = None,
    ) -> List:

        query = self.build_query(
            search, asset_class, end, max_price, min_price, start, trade_type
        )
        ret = self.collection.find(query, projection={"_id": False})
        return list(ret)

    def build_query(
        self, search, asset_class, end, max_price, min_price, start, trade_type
    ) -> Dict:

        query = {"$and": []}

        if search:
            query["$and"].append(
                {
                    "$or": [
                        {"counterparty": {"$regex": search, "$options": "i"}},
                        {"instrumentId": {"$regex": search, "$options": "i"}},
                        {"instrumentName": {"$regex": search, "$options": "i"}},
                        {"trader": {"$regex": search, "$options": "i"}},
                    ]
                }
            )

        if asset_class:
            query["$and"].append(
                {"assetClass": {"$regex": asset_class, "$options": "i"}}
            )

        if start:
            query["$and"].append(
                {"tradeDateTime": {"$gte": start}}
            )

        if end:
            query["$and"].append(
                {"tradeDateTime": {"$lte": end}}
            )

        if max_price:
            query["$and"].append(
                {"tradeDetails.price": {"$lte": max_price}}
            )

        if min_price:
            query["$and"].append(
                {"tradeDetails.price": {"$gte": min_price}}
            )

        if trade_type:
            query["$and"].append(
                {"tradeDetails.buySellIndicator": {"$regex": trade_type, "$options": "i"}}
            )

        if len(query["$and"]) == 0:
            return {}

        return query

    def load_db(self) -> None:
        data_test = generate_random_data_test()
        self.collection.insert_many(data_test)

    def start_client(self) -> MongoClient:
        client = MongoClient()

        return client

    def teardown(self) -> None:
        self.client.close()
