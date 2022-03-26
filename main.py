import webcheck
import requests
from constants import *
from backend import database

res1 = requests.get(GOOGLE_URL)
res2 = requests.get(BING_URL)

# retrieves data from the sdk and adds call the backend function to add it to the db
database.insert_data_to_db(webcheck.get_data())


# tests
print(database.queries.get_data_by_id('762f7b56cb2544d9a4421b890fd604aa'))
print(database.queries.get_most_commonly_visited_website())
print(database.queries.get_data_by_timeframe(start_time=0, end_time=1647803542.988812))
