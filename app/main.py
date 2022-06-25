from fastapi import FastAPI
from .mongoclient import MongoSteeleye
from .schemas import Trade
from typing import List


app = FastAPI()
db = MongoSteeleye()


@app.get("/")
async def root():
    return {"ok": True}

@app.get("/fetch-all/", response_description="List all trades", response_model=List[Trade])
def fetch_all():
    """
    Function used to return all the items on db

    :param string anything: Anything that can be used
    :return: List of all the data
    :rtype: list of dicts
    :raises TransactionError: If there is an error we return TransactionError
    """
    trades = db.make_query()

    return trades

@app.get("/fetch-item/", response_description="Fetch single trade by trade id", response_model=List[Trade])
def fetch_item(id):
    """
    Function used to return single item from db

    :param string id: Id to search on the database
    :return: Dict representation of the item
    :rtype: List with single dict
    :raises TransactionError: If there is an error we return TransactionError
    """
    trade = db.make_query({"tradeId": id})

    return trade
