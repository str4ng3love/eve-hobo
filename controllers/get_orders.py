import requests
from utils.helpers import concat, filter_jita44, sortByTypeID, concatSameTypeIDs, sortByPriceAsc, sortByPriceDesc


def get_pages(order_type):
    url = 'https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility'
    url = url+'&order_type='+order_type

    resp = requests.get(url)

    pagesAmount = int(resp.headers['X-Pages'])
    pages = []
    try:
        while (pagesAmount > 0):
            paginatedUrl = url+'&page='+str(pagesAmount)
            page = requests.get(paginatedUrl)
            page = page.json()
            pages.append(page)
            pagesAmount = pagesAmount - 1

    except requests.exceptions.RequestException as e:
        print("Error occurred during API request:", e)
        return None
    return pages


def get_buy_orders():
    orders = get_pages("buy")
    concatedOrders = concat(orders)
    jita_orders = list(filter(filter_jita44, concatedOrders))
    sortedOrders = sortByTypeID(jita_orders)
    listOfSameTypeOrders = concatSameTypeIDs(sortedOrders)
    for l in listOfSameTypeOrders:
        sortByPriceDesc(l)
    return listOfSameTypeOrders


def get_sell_orders():
    orders = get_pages("sell")
    concatedOrders = concat(orders)
    jita_orders = list(filter(filter_jita44, concatedOrders))
    sortedOrders = sortByTypeID(jita_orders)
    listOfSameTypeOrders = concatSameTypeIDs(sortedOrders)
    for l in listOfSameTypeOrders:
        sortByPriceAsc(l)
    return listOfSameTypeOrders


def get1pageBuy():
    url = 'https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=buy&page=1'

    resp = requests.get(url)
    data = resp.json()
    jitaOrders = list(filter(filter_jita44, data))
    sortedOrders = sortByTypeID(jitaOrders)
    listOfSameTypeOrders = concatSameTypeIDs(sortedOrders)

    result = listOfSameTypeOrders
    return result
