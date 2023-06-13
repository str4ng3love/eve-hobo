
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
    return result

def concatSameTypeIDs(orders):
    sortedOrders = []
    newArray = []

   
    for o in orders:
        if len(newArray) == 0:
            newArray.append(o)
           
           
        elif newArray[-1]['type_id'] == o['type_id']:
            newArray.append(o) 
        else:
            sortedOrders.append(newArray)
            newArray = []
            newArray.append(o)
          
            
    return sortedOrders

def sortByPriceAsc(orders:list):

    orders.sort(key=lambda k:k['price'])
    return orders
def sortByPriceDesc(orders:list):

    orders.sort(key=lambda k:k['price'], reverse=True)
    return orders
def sortByTypeID(orders:list):
    orders = sorted(orders, key=lambda k:k['type_id'])

    return orders


# def concatSameTypeIDs(orders):
#     sortedOrders = []
#     sortedIndex = 0
   
#     for o in orders:
#         if len(sortedOrders) == 0:
#             newEntry = {}
#             newEntry['type_id'] =  o['type_id']
#             newEntry['orders'] = [o]
#             sortedOrders.append(newEntry)
         
           
#         elif sortedOrders[sortedIndex]['type_id'] == o['type_id']:
#             sortedOrders[sortedIndex]['orders'].append(o) 
#         else:
#             newEntry = {}
#             newEntry['type_id'] =  o['type_id']
#             newEntry['orders'] = [o]
#             sortedOrders.append(newEntry)
#             sortedIndex +=1
            
#     return sortedOrders