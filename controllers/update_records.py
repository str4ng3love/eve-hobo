from db.pymongo_get_db import get_database
import sys

sys.path.append('../db')

dbname = get_database()
collection_name = dbname["Items"]
result = []
def update_buy_orders(orders:list):
    print('Updating buy orders...')
    for o in orders:
       items = collection_name.update_one({"type_id": o[-1]["type_id"]}, {"$set": {"buy_orders": o}}, upsert=True)
       result.append(items.modified_count)

    return result
def update_sell_orders(orders:list):
    print('Updating sell orders...')
    for o in orders:
       items = collection_name.update_one({"type_id": o[-1]["type_id"]}, {"$set": {"sell_orders": o}}, upsert=True)
       result.append(items.modified_count)

    return result

