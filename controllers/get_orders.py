import requests

def filter_jita44(order):
    stationId = 60003760
    if order['location_id'] == stationId:
        return True
    else:
        return False

def concat(listOfLists: list):
    result = []
    for l in listOfLists:
        if isinstance(l, list):
            result = result + l
    print(len(result))
    return result


def get_pages(order_type):
    url = 'https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility'
    url = url+'&order_type='+order_type

    resp = requests.get(url)

    pagesAmount = int(resp.headers['X-Pages'])
    print(pagesAmount)
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
    return jita_orders


def get_sell_orders():
    orders = get_pages("sell")
    concatedOrders = concat(orders)
    jita_orders = list(filter(filter_jita44, concatedOrders))
    return jita_orders

