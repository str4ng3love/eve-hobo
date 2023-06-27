from controllers.get_records import getOrdersBlob
from utils.helpers import filter_jita44, concat, concatSameTypeIDs, sortByPriceAsc, sortByPriceDesc, sortByTypeID 


def find_profits(order_type, searchMethod, amount):
    
    orders = getOrdersBlob(order_type)
    print("Concating...")
    # concatedOrders = concat(orders)
    # print("Filtering...")
    # jitaOrders = list(filter(filter_jita44, concatedOrders))
    # print("Sorting...")
    # sortedOrders = sortByTypeID(jitaOrders)
    # print("Concating same type_id orders...")
    # sameOrders = concatSameTypeIDs(sortedOrders)
    # if order_type == 'buy_orders':
    #     sortedOrders = sortByPriceDesc(sameOrders)
    # else:
    #     sortedOrders = sortByPriceAsc(jitaOrders)
    print('Done')
    print(len(orders))
    return orders

# todo: extract buy orders from object