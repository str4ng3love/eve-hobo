from db.pymongo_get_db import get_database
from utils.helpers import concat
from controllers.utilities import get_reprocessed_values, filter_and_sort_orders_blob
import sys
import time

sys.path.append('../db')

dbname = get_database()
collection_name1 = dbname["Items"]
collection_name2 = dbname["Orders"]
collection_name3 = dbname["Materials"]
collection_name4 = dbname["MatsOrders"]
result = []


def updateOrdersBlob(orders: list, orders_type: str):
    """
    orders: List of pages with orders from ESI. \n
    orders_type: String defining type of orders to update. Must be either "buy_orders" or "sell_orders".
    """

    if isinstance(orders, list) and isinstance(orders_type, str):
        cursor1 = collection_name2.delete_many(
            {orders_type: {"$exists": True}})
        print("Deleted " + str(cursor1.deleted_count) + " db entries...")
        print('Updating '+orders_type+' blob...')
        inserted = []
        ordersAmount = len(orders)
        start_time = time.time()
        for o in orders:
            cursor = collection_name2.insert_one({orders_type: o})
            inserted.append(cursor.inserted_id)
            print(str(ordersAmount) + " remaining pages to insert.")
            ordersAmount -= 1
        print("Done inserting documents in --- %s seconds ---" %
              (time.time() - start_time))
        print('Updating materials buy order prices...')
        cursor4 = collection_name4.delete_many(
            {orders_type: {"$exists": True}})
        print("Deleted " + str(cursor4.deleted_count) + " db entries...")
        concatedOrders = concat(orders)
        sortedAndFilteredOrders = filter_and_sort_orders_blob(concatedOrders, orders_type)
        reprocessHighestPrice = get_reprocessed_values(sortedAndFilteredOrders)
        entriesAmount = len(reprocessHighestPrice)
        for i in reprocessHighestPrice:
            cursor = collection_name4.insert_one({orders_type: i})
            entriesAmount -= 1
            print(str(entriesAmount) + " remaining material prices to insert.")
        return {"message": "Inserted " + str(len(inserted)) + " pages. Material buy order prices updated."}
    else:
        raise ValueError('Parameters received have wrong type, expected list, str, got ' +
                         str(type(orders))+', ' + str(type(orders_type)))
