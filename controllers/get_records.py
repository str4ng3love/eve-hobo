from db.pymongo_get_db import get_database
import sys
import time
from time import strftime, localtime
import re
sys.path.append('../db')

dbname = get_database()
items = dbname["Items"]
buy_orders = dbname["BuyOrders"]
sell_orders = dbname["SellOrders"]
materials = dbname["Materials"]
mats_orders_buy = dbname["MatsOrdersBuy"]
mats_orders_sell = dbname["MatsOrdersSell"]
result = []


def getOrdersBlob(orders_type: str):
    """
        orders_type: String defining type of orders to download from DB. Must be either "buy_orders" or "sell_orders".
        Returns a list of specified orders.
    """
    if orders_type == "buy_orders":
        count = buy_orders.count_documents({})
        if count > 0:
            print("Attempting to download " + str(count) +
                  " documents from database...")
            start_time = time.time()
            orders =[]
            cursor = buy_orders.find({}, {"_id": 0}).sort("$natural", 1)
            cursor.allow_disk_use(True)
            cursor.max_await_time_ms(max_await_time_ms=10000)
            cursor.next()
            print(cursor.explain())
            for o in cursor: 
                orders.append(o)
            print('Documents downloaded in %s seconds.' %
                  (time.time() - start_time))
            
            return orders
        else:
            print('There are no '+orders_type+' in the DB...')
            return 'There are no '+orders_type+' in the DB...'
    else:
        count = sell_orders.count_documents({})
        if count > 0:
            print("Attempting to download " + str(count) +
                  " documents from database...")
            start_time = time.time()
            orders =[]
            cursor = sell_orders.find({}, {"_id": 0}).sort("$natural", 1)
         
            for o in cursor: 
                orders.append(o)
            print('Documents downloaded in %s seconds.' %
                  (time.time() - start_time))

            return orders
        else:
            print('There are no '+orders_type+' in the DB...')
            return 'There are no '+orders_type+' in the DB...'


def getTELBuySave():
    """
        Returns last buy orders update date.
    """
    
    cursor = list(buy_orders.find({"buy_orders": {"$exists": True}}).limit(1))
    
    if len(cursor) == 0:
        return "DB is empty"
    else:
        id = str(cursor[0]['_id'])
        slicer = slice(0, 8)
        secs = int(id[slicer], 16)
        date = localtime(secs)
        humanReadableDate = strftime('%Y-%m-%d %H:%M:%S', date)

        return humanReadableDate


def getTELSellSave():
    """
        Returns last sell orders update date.
    """
    cursor = list(sell_orders.find({"sell_orders": {"$exists": True}}).limit(1))

    if len(cursor) == 0:
        return "DB is empty"
    else:
        id = str(cursor[0]['_id'])
        slicer = slice(0, 8)
        secs = int(id[slicer], 16)
        date = localtime(secs)
        humanReadableDate = strftime('%Y-%m-%d %H:%M:%S', date)

        return humanReadableDate


def getMaterials():
    """
        Returns a list of materials used in industry.
    """
    cursor = list(materials.find({}, {"_id": 0}))
    return cursor


def getMaterialByTypeId(type_id: int):
    """
        Returns a material.
    """
    cursor = materials.find_one({"type_id": int(type_id)}, {"_id": 0})

    if cursor == None:
        return {"error": "No entry associated with type_id: " + str(type_id)+" Make sure to provide int value"}
    else:
        return cursor


def getMaterialsByString(string: str):
    """
        Returns a list of materials with names containing string:str.
    """
    # if name
    regex = "[A-Za-z0-9._()'$%!:]"
    if re.match(regex, string):
        cursor = list(materials.find(
            {"name": {"$regex":  str(string), "$options": "i"}}, {"_id": 0}))

        if len(cursor) == 0:
            return {"error": "No entry associated with string: " + str(string)}
        else:
            return cursor
    else:
        return {"error": "Invalid string:str"}


def getItems():
    """
        Returns a list of items.
    """
    cursor = list(items.find({}, {"_id": 0}))

    return cursor


def getMatsBuyPrice():
    """
        Returns a list of materials with their current highest buy market price.
    """
    cursor = list(mats_orders_buy.find(
        {}, {"_id": 0}))
    orders = []
    for c in cursor:

        orders.append(c['buy_orders'])
    return orders


def getMatsSellPrice():
    """
        Returns a list of materials with their current lowest sell market price.
    """
    cursor = list(mats_orders_sell.find(
        {}, {"_id": 0}))
    orders = []
    for c in cursor:

        orders.append(c['sell_orders'])
    return orders


def getItemsReprocessable():
    """
        Returns a list of reprocessable items.
    """

    cursor = list(items.find(
        {"reprocess": {"$exists": True}}, {"_id": 0}))

    return cursor


def getItemByTypeId(type_id: int):
    """
        Returns an item.
    """
    cursor = items.find_one({"type_id": int(type_id)}, {"_id": 0})

    if cursor == None:
        return {"error": "No entry associated with type_id: " + str(type_id)+" Make sure to provide int value"}
    else:
        return cursor


def getItemsByString(string: str):
    """
        Returns a list of items with names containing string:str.
    """
    regex = "[A-Za-z0-9._()'$%!:]"
    if re.match(regex, string):
        cursor = list(items.find(
            {"name": {"$regex":  str(string), "$options": "i"}}, {"_id": 0}))

        if len(cursor) == 0:
            return {"error": "No entry associated with string: " + str(string)}
        else:
            return cursor
    else:
        return {"error": "Invalid string:str"}
