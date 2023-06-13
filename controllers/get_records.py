from db.pymongo_get_db import get_database
import sys
sys.path.append('../db')

dbname = get_database()
collection_name = dbname["Items"]
result = []
def get_orders():

    
    orders = list(collection_name.find({}, {"name":1, "_id": 0, "buy_orders": 1}))
  

    return orders