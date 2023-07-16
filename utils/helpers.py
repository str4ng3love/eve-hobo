
import datetime


def filter_jita44(order):
    stationId =60003760
    if order['location_id'] == stationId:
        return True
    else:
        return False
    
def filter_amarr_oris(order):
    stationId =60008494
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


def sortByPriceAsc(orders: list):
    
    orders.sort(key=lambda k: k['price'])
    return orders


def sortByPriceDesc(orders: list):
    orders.sort(key=lambda k: k['price'], reverse=True)
    return orders


def sortByTypeID(orders: list):
    orders = sorted(orders, key=lambda k: k['type_id'])

    return orders


def timeSinceInput(timeInput: str, evalValue: int = None):
    """
    Takes ISO formated date and returns difference since datetime.datetime.now() in 'X days, X hours, X minutes, X secs.
    Optional: evalValue takes a value in minutes, and checks whether specified amount have passed since timeInput.
    """
    now = datetime.datetime.now()
    timeVar = datetime.datetime.fromisoformat(timeInput)
    diff = now - timeVar
    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = minutes % 60

    if evalValue != None:

        if evalValue * 60 < diff.seconds or hours > 0 or days > 0:
            evaluation = True
        else:
            evaluation = False

        return {'time': '{} days, {} hours, {} minutes, {} seconds '.format(days, hours, minutes, hours), "evaluation": evaluation}
    else:
        return {'time': '{} days, {} hours, {} minutes, {} seconds '.format(days, hours, minutes, hours)}

