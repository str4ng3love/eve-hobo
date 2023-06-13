from db.pymongo_get_db import get_database
import sys
sys.path.append('../db')

dbname = get_database()
collection_name = dbname["Items"]
result = []
def update_buy_orders(orders:list):

    for o in orders:
       items = collection_name.update_one({"type_id": o[-1]["type_id"]}, {"$set": {"buy_orders": o}}, upsert=True)
       result.append(items)

    return result