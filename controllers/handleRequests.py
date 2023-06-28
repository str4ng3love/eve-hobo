from controllers.get_records import getOrdersBlob, getMaterials, getItemsReprocessable
from utils.helpers import filter_jita44, concat, concatSameTypeIDs, sortByPriceAsc, sortByPriceDesc, sortByTypeID


def get_filtered_and_sorted_orders(orders_type):

    orders = getOrdersBlob(orders_type)
    print("Concating...")
    extractedOrders = []
    for o in orders:
        extractedOrders.append(o[orders_type])
    concatedOrders = concat(extractedOrders)
    print("Filtering...")
    jitaOrders = list(filter(filter_jita44, concatedOrders))
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




# def get_reprocessed_values
# todo: calc reprocess value