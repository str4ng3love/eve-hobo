from db.pymongo_get_db import get_database
from utils.helpers import concat
from controllers.utilities import get_reprocessed_values, filter_and_sort_orders_blob
import sys
import time

sys.path.append('../db')

dbname = get_database()
items = dbname["Items"]
buy_orders = dbname["BuyOrders"]
sell_orders = dbname["SellOrders"]
materials = dbname["Materials"]
material_prices_buy = dbname["MatsOrdersBuy"]
material_prices_sell = dbname["MatsOrdersSell"]
result = []


def updateOrdersBlob(orders: list, orders_type: str):
    """
    orders: List of pages with orders from ESI. \n
    orders_type: String defining type of orders to update. Must be either "buy_orders" or "sell_orders".
    """

    if isinstance(orders, list) and isinstance(orders_type, str):
        inserted = []
        ordersAmount = len(orders)
        start_time = time.time()
        if orders_type == 'buy_orders':
            cursor = buy_orders.delete_many({})
            print("Deleted " + str(cursor.deleted_count) + " db entries...")
            print('Updating '+orders_type+' blob...')
            for o in orders:
                cursor = buy_orders.insert_one({"buy_orders": o})
                inserted.append(cursor.inserted_id)
                print(str(ordersAmount) + " remaining pages to insert.")
                ordersAmount -= 1
            print("Done inserting documents in --- %s seconds ---" %
                  (time.time() - start_time))
            cursor = material_prices_buy.delete_many({})
            print("Deleted " + str(cursor.deleted_count) + " db entries...")
            concatedOrders = concat(orders)
            sortedAndFilteredOrders = filter_and_sort_orders_blob(
                concatedOrders, orders_type)
            reprocessHighestPrice = get_reprocessed_values(
                sortedAndFilteredOrders)
            entriesAmount = len(reprocessHighestPrice)
            for i in reprocessHighestPrice:
                cursor = material_prices_buy.insert_one({orders_type: i})
                entriesAmount -= 1
                print(str(entriesAmount) + " remaining material prices to insert.")
        else:
            cursor = sell_orders.delete_many(
                {orders_type: {"$exists": True}})
            print("Deleted " + str(cursor.deleted_count) + " db entries...")
            print('Updating '+orders_type+' blob...')
            for o in orders:
                cursor = sell_orders.insert_one({"sell_orders": o})
                inserted.append(cursor.inserted_id)
                print(str(ordersAmount) + " remaining pages to insert.")
                ordersAmount -= 1
            print("Done inserting documents in --- %s seconds ---" %
                  (time.time() - start_time))
            print('Updating materials buy order prices...')
            cursor = material_prices_sell.delete_many({})
            print("Deleted " + str(cursor.deleted_count) + " db entries...")
            concatedOrders = concat(orders)
            sortedAndFilteredOrders = filter_and_sort_orders_blob(
                concatedOrders, orders_type)
            reprocessHighestPrice = get_reprocessed_values(
                sortedAndFilteredOrders)
            entriesAmount = len(reprocessHighestPrice)
            for i in reprocessHighestPrice:
                cursor = material_prices_sell.insert_one({orders_type: i})
                entriesAmount -= 1
                print(str(entriesAmount) + " remaining material prices to insert.")

        return {"message": "Inserted " + str(len(inserted)) + " pages. Material order prices updated."}
    else:
        raise ValueError('Parameters received have wrong type, expected list, str, got ' +
                         str(type(orders))+', ' + str(type(orders_type)))
