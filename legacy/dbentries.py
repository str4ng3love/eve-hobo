from db.pymongo_get_db import get_database
import json
import sys
sys.path.append('../db')

with open('typeNamesAndReprocess.json', 'r') as f:
    data = json.load(f)


dbname = get_database()
collection_name = dbname["Items"]

items = collection_name.insert_many(data)