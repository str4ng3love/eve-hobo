from controllers.get_records import getOrdersBlob, getMaterials, getItems
from utils.helpers import filter_jita44, concat, concatSameTypeIDs, sortByPriceAsc, sortByPriceDesc, sortByTypeID


def get_filtered_and_sorted_orders(order_type):

    orders = getOrdersBlob(order_type)
    print("Concating...")
    extractedOrders = []
    for o in orders:
        extractedOrders.append(o[order_type])
    concatedOrders = concat(extractedOrders)
    print("Filtering...")
    jitaOrders = list(filter(filter_jita44, concatedOrders))
    print("Sorting...")
    sortedOrders = sortByTypeID(jitaOrders)
    print("Concating same type_id orders...")
    sameTypeOrders = concatSameTypeIDs(sortedOrders)
    if order_type == 'buy_order':
        for o in sameTypeOrders:
            sortByPriceDesc(o)
    else:
        for o in sameTypeOrders:
            sortByPriceAsc(o)

    
    return sameTypeOrders


# def get_items_industry(orders):
#     type_ids = []
#     for o in orders:
#         type_ids.append(o[0]['type_id'])
#     items = getItems()
#     for id in type_ids:
        
# def find_profits(orders, method, amount):
    
