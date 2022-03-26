import pymongo
from . import utils
from .database_queries import Queries

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["mydatabase"]

requests_data_col = db["requests_data"]


def insert_data_to_db(data_dict) -> None:
    parsed_data = utils.prepare_data_for_db(data_dict)
    requests_data_col.insert_many(parsed_data)


queries = Queries(requests_data_col)


