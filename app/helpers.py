import random
import datetime
import uuid

def generate_random_data_test(quantity=10):
    """
    Function used to generate the test data

    :param int quantity: How many items will be generated
    :return: List of all the data
    :rtype: list of dicts
    """
    asset_classes = ["Equity", "Bond", "FX"]
    instruments = ["TSLA", "AAPL", "AMZN"]
    bs_indicator = ["BUY", "SELL"]

    data_test = []
    for i in range(quantity):
        data_test.append(
            {
                #"id": str(random.randint(1, 10000)),
                "assetClass": random.choice(asset_classes),
                "counterparty": "sadadsadad",
                "instrumentId": random.choice(instruments),
                "instrumentName": "Name",
                "tradeDateTime": datetime.datetime.now(),
                "tradeDetails": {
                    "buySellIndicator": random.choice(bs_indicator),
                    "quantity": random.randint(1, 200),
                    "price": round(random.uniform(12.4, 903.87), 2),
                },
                "tradeId": str(random.randint(1, 10000)),
                "trader": "Breno Carvalho",
            }
        )

    return data_test