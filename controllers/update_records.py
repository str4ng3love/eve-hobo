from db.pymongo_get_db import get_database
import sys

sys.path.append('../db')

dbname = get_database()
collection_name1 = dbname["Items"]
collection_name2 = dbname["Orders"]
result = []

def update_orders_blob(orders:list, orders_type:str):
    """
    orders: List of pages with orders from ESI. \n
    orders_type: String defining type of orders to update. Must be either "buy_orders" or "sell_orders".
    """
  
    if isinstance(orders, list) and isinstance(orders_type, str):
      cursor1 = collection_name2.delete_many({orders_type: {"$exists": True}})
      print("Deleted " + str(cursor1.deleted_count) +" db entries...")
      print('Updating '+orders_type+' blob...')
      inserted = []
      ordersAmount = len(orders)
      for o in orders:
        cursor = collection_name2.insert_one({orders_type: o})
        inserted.append(cursor.inserted_id)
        print(str(ordersAmount) +" remaining pages to insert.")
        ordersAmount -= 1
      print("Done inserting documents.")
      return "Inserted " +str(len(inserted))+ " pages."
    else:
        raise ValueError('Parameters received have wrong type, expected list, str, got '+ str(type(orders))+', '+ str(type(orders_type)))
