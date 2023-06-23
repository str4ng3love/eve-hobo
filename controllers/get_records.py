from db.pymongo_get_db import get_database
import sys
import time
from time import strftime, localtime

sys.path.append('../db')

dbname = get_database()
collection_name1 = dbname["Items"]
collection_name2 = dbname["Orders"]
result = []

def get_orders():

    
    orders = list(collection_name1.find({}, {"_id": 0, "name": 1, "type_id": 1, "reprocess": 1, "portion_size": 1, "buy_orders": 1, "sell_orders": 1}))

    return orders

def test_get():

    orders = list(collection_name1.find({"type_id": 18},{"_id": 0, }))
  

    return orders

def get_orders_blob(orders_type:str):
    """
    orders_type: String defining type of orders to download from DB. Must be either "buy_orders" or "sell_orders".
    """
    count = collection_name2.count_documents({orders_type: {"$exists": True}})
    if count > 0:
        print("Attempting to download "+ str(count) +" documents from database...")
        start_time = time.time()
        orders = list(collection_name2.find({orders_type: {"$exists": True}}, {"_id": 0}))
        print('Documents downloaded in %s seconds.' % (time.time() - start_time))
        
        return orders
    else:
        print('There are no '+orders_type+' in the DB...')
        return 'There are no '+orders_type+' in the DB...'
def get_TEL_buy_save():
    """
    Performs a DB call to check when last buy orders update occured.
    """
    cursor = list(collection_name2.find({"buy_orders": {"$exists": True}}).limit(1))
    
    if len(cursor)==0:
        return "DB is empty"
    else:
        id = str(cursor[0]['_id'])
        slicer = slice(0,8)    
        secs = int(id[slicer], 16)
        date =  localtime(secs)
        humanReadableDate = strftime('%Y-%m-%d %H:%M:%S', date)

        return humanReadableDate
   

def get_TEL_sell_save():
    """
    Performs a DB call to check when last sell orders update occured.
    """
    cursor = list(collection_name2.find({"sell_orders": {"$exists": True}}, {"_id"}).limit(1))
    
    if len(cursor)==0:
        return "DB is empty"
    else:
        id = str(cursor[0]['_id'])
        slicer = slice(0,8)    
        secs = int(id[slicer], 16)
        date =  localtime(secs)
        humanReadableDate = strftime('%Y-%m-%d %H:%M:%S', date)

        return humanReadableDate