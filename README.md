# SteelEye technical test

## Stack

- Python
- FastAPI
- MongoDB
- Pydantic

## Steps to test

Since we are using FastAPi, the easiest way to test is:

1. Run the command `uvicorn app.main:app --reload` on your terminal from the project root
2. Access `http://127.0.0.1:8000/docs` to use the OpenAPI interface to use the endpoints

### Explanation of the solution

For the database I chose to use MongoDB for two reasons:

- I have some experience with Mongo, what makes it easier for me
- `pymongo_inmemory` wich is a lib that allows me to create a local Mongo database and mock the data

I implemented a interface with this MongoDB database and used it to fetch the data.
The queries are built to support any of the filters combined between themselves

The `main.py` file has two endpoints, one for fetching all the trades, and another one for a single trade by its trade_id

Both of this endpoints returns lists, just to keep a pattern.

### Random data generation

The test data is generated on the `helpers.py` file is randomized between some data that I got from the examples on the schema models provided by you on the test description
