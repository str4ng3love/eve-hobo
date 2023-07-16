from controllers.get_records import getMaterials,  getOrdersBlob
from utils.helpers import filter_jita44, concat, concatSameTypeIDs, sortByPriceAsc, sortByPriceDesc, sortByTypeID
import math


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


def prepareItems(items, buyPrice, sellPrice):
    baseReprocessReturn = 0.5
    for i in items:
        matsBuyValue = 0
        matsSellValue = 0
        for k, v in i['reprocess'].items():
            for bp in buyPrice:

                if int(k) == bp['type_id']:
                    matsAmount = 0
                    if (v * baseReprocessReturn % 1) >= 0.5:
                        matsAmount = math.floor(v * baseReprocessReturn)
                    else:
                        matsAmount = math.ceil(v * baseReprocessReturn)

                    matsBuyValue = matsBuyValue + matsAmount * bp['price']
                    i['mats_buy_value'] = matsBuyValue
            for sp in sellPrice:

                if int(k) == sp['type_id']:
                    matsAmount = 0
                    if (v * baseReprocessReturn % 1) >= 0.5:
                        matsAmount = math.floor(v * baseReprocessReturn)
                    else:
                        matsAmount = math.ceil(v * baseReprocessReturn)
                    matsSellValue = matsSellValue + matsAmount * sp['price']
                    i['mats_sell_value'] = matsSellValue
    return items
