from db.pymongo_get_db import get_database
import sys
import time
from time import strftime, localtime
import re
sys.path.append('../db')

dbname = get_database()
collection_name1 = dbname["Items"]
collection_name2 = dbname["Orders"]
collection_name3 = dbname["Materials"]
result = []


def getOrdersBlob(orders_type: str):
    """
        orders_type: String defining type of orders to download from DB. Must be either "buy_orders" or "sell_orders".
        Returns a list of specified orders.
    """
    count = collection_name2.count_documents({orders_type: {"$exists": True}})
    if count > 0:
        print("Attempting to download " + str(count) +
              " documents from database...")
        start_time = time.time()
        orders = list(collection_name2.find(
            {orders_type: {"$exists": True}}, {"_id": 0}))
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
    cursor = list(collection_name2.find(
        {"buy_orders": {"$exists": True}}).limit(1))

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
    cursor = list(collection_name2.find(
        {"sell_orders": {"$exists": True}}, {"_id"}).limit(1))

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
    cursor = list(collection_name3.find({}, {"_id": 0}))
    return cursor


def getMaterialByTypeId(type_id: int):
    """
        Returns a material.
    """
    cursor = collection_name3.find_one({"type_id": int(type_id)}, {"_id": 0})

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
        cursor = list(collection_name3.find(
            {"name": {"$regex":  str(string), "$options": "i"}}, {"_id": 0}))
        print(len(cursor))
        if len(cursor) == 0:
            return {"error": "No entry associated with string: " + str(string)}
        else:
            return cursor
    else: 
        return {"error": "Invalid string:str"}


def getItemsList():
    """
        Returns a list of items.
    """
    cursor = list(collection_name1.find({}, {"_id": 0}))

    return cursor

def getItemByTypeId(type_id: int):
    """
        Returns an item.
    """
    cursor = collection_name1.find_one({"type_id": int(type_id)}, {"_id": 0})

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
        cursor = list(collection_name1.find(
            {"name": {"$regex":  str(string), "$options": "i"}}, {"_id": 0}))

        if len(cursor) == 0:
            return {"error": "No entry associated with string: " + str(string)}
        else:
            return cursor
    else: 
        return {"error": "Invalid string:str"}