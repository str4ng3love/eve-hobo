import requests

import time



def get_pages(orders_type:str):
    """
    orders_type: Specify the kind of orders to be downloaded. Must be str, either "buy" or "sell"
    """
    if isinstance(orders_type, str):
        url = 'https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility'
        url = url+'&order_type='+orders_type

        resp = requests.get(url)

        pagesAmount = int(resp.headers['X-Pages'])
        pages = []
        print('Attempting to download orders data...')
        start_time = time.time()
        try:
            while (pagesAmount > 0):
                print("Pages to go: " +str(pagesAmount))
                paginatedUrl = url+'&page='+str(pagesAmount)
                page = requests.get(paginatedUrl)
                page = page.json()
                pages.append(page)
                pagesAmount = pagesAmount - 1
                
        except requests.exceptions.RequestException as e:
            print("Error occurred during API request:", e)
            return None
        print('Done downloading orders in --- %s seconds ---' % (time.time() - start_time) )
        
        return pages
    else:
        raise ValueError('Parameter received has wrong type, expected str, got '+ str(type(orders_type)))

# def get_buy_orders():
#     orders = get_pages("buy")
#     concatedOrders = concat(orders)
#     jita_orders = list(filter(filter_jita44, concatedOrders))
#     sortedOrders = sortByTypeID(jita_orders)
#     listOfSameTypeOrders = concatSameTypeIDs(sortedOrders)
#     for l in listOfSameTypeOrders:
#         sortByPriceDesc(l)
#     return listOfSameTypeOrders
#     return orders


# def get_sell_orders():
#     orders = get_pages("sell")
#     concatedOrders = concat(orders)
#     jita_orders = list(filter(filter_jita44, concatedOrders))
#     sortedOrders = sortByTypeID(jita_orders)
#     listOfSameTypeOrders = concatSameTypeIDs(sortedOrders)
#     for l in listOfSameTypeOrders:
#         sortByPriceAsc(l)
#     return listOfSameTypeOrders
