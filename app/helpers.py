import random
import datetime
from typing import List


def generate_random_data_test(quantity: int = 10) -> List:
    """
    Function used to generate the test data

    :param int quantity: How many items will be generated
    :return: List of all the data
    :rtype: list of dicts
    """

    # The lists below are used to generate some random data
    # to be later inserted on the mongo collection
    asset_classes = ["Equity", "Bond", "FX"]
    instruments = ["TSLA", "AAPL", "AMZN"]
    bs_indicator = ["BUY", "SELL"]
    traders = ["Breno", "Bob Smith", "bob smith", "Breno Carvalho"]
    counterparties = ["Bank X", "Investment Bank Y", "Stockbroker Z"]

    data_test = []
    for i in range(quantity):
        data_test.append(
            {
                "assetClass": random.choice(asset_classes),
                "counterparty": random.choice(counterparties),
                "instrumentId": random.choice(instruments),
                "instrumentName": "Name",
                "tradeDateTime": datetime.datetime.now(),
                "tradeDetails": {
                    "buySellIndicator": random.choice(bs_indicator),
                    "quantity": random.randint(1, 200),
                    "price": round(random.uniform(12.4, 903.87), 2),
                },
                "tradeId": str(random.randint(1, 10000)),
                "trader": random.choice(traders),
            }
        )

    return data_test
