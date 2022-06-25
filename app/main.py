from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI

from .mongoclient import MongoSteeleye
from .schemas import Trade


app = FastAPI()
db = MongoSteeleye()


@app.get("/")
async def root():
    return {"ok": True}


@app.get(
    "/fetch-all/", response_description="List all trades", response_model=List[Trade]
)
def fetch_all(
    text_search: Optional[str] = None,
    asset_class: Optional[str] = None,
    end: Optional[datetime] = None,
    max_price: Optional[str] = None,
    min_price: Optional[str] = None,
    start: Optional[datetime] = None,
    trade_type: Optional[str] = None,
):
    """
    Function used to return all the items on db

    :param string text_search: String used to search through some fields
    :return: List of all the data
    :rtype: List of dicts
    """
    trades = db.make_query(
        search=text_search,
        asset_class=asset_class,
        end=end,
        max_price=max_price,
        min_price=min_price,
        start=start,
        trade_type=trade_type,
    )

    return trades

@app.get(
    "/fetch-item/",
    response_description="Fetch single trade by trade id",
    response_model=List[Trade],
)
def fetch_item(id):
    """
    Function used to return single item from db

    :param string id: Id to search on the database
    :return: Dict representation of the item
    :rtype: List with single dict
    """
    trade = db.make_query({"tradeId": id})

    return trade
