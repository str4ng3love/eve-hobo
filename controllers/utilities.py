from controllers.get_records import  getMaterials
from utils.helpers import filter_jita44, concat, concatSameTypeIDs, sortByPriceAsc, sortByPriceDesc, sortByTypeID
import json
def get_reprocessed_values(orders):
    mats = getMaterials()
    matsWithPrice = []
    for o in orders:
        for m in mats:

            if m['type_id'] == o[0]['type_id']:

                newEntry = m
                newEntry['price'] = o[0]['price']
                matsWithPrice.append(newEntry)
   
    return matsWithPrice

def filter_and_sort_orders_blob(orders, orders_type):
    print("Filtering...")
    jitaOrders = list(filter(filter_jita44, orders))
    print("Sorting...")
    sortedOrders = sortByTypeID(jitaOrders)
    print("Concating same type_id orders...")
    sameTypeOrders = concatSameTypeIDs(sortedOrders)
    if orders_type == 'buy_orders':
        for o in sameTypeOrders:
            sortByPriceDesc(o)
    else:
        for o in sameTypeOrders:
            sortByPriceAsc(o)

    return sameTypeOrders
