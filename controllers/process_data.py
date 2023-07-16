from controllers.utilities import get_filtered_and_sorted_orders, prepareItems
from controllers.get_records import getItemsReprocessable, getMatsBuyPrice, getMatsSellPrice
import time


def findDealsByMethod(orders_type:str, method: str, amount: int, searchThru: str, reprocessSkillValue: int = None):
    """ 
        orders_type = 'buy_orders' | 'sell_orders'
        method:str = p'ercentage' | 'amount' \n
        amount:int > 0 \n
        searchThru:str = 'sell' | 'buy' \n
        reprocessSkill = [0-5], default = 0
    """
    if amount == 0:
        return {'error': 'Please provide a positive value.'}
    if amount < 0:
        amount = abs(amount)
    baseReprocessReturn = 0.5
    reprocessSkill = reprocessSkillValue if reprocessSkillValue else 0
    baseReprocessReturn + reprocessSkill * 0.02
    goodStuff = []
    orders = get_filtered_and_sorted_orders(orders_type)
    buyPrice = getMatsBuyPrice()
    sellPrice = getMatsSellPrice()
    items = getItemsReprocessable()
    preped = prepareItems(items, buyPrice, sellPrice)
    ordersLen = len(orders)
    print('Processing ' + str(ordersLen) + ' entries.')
    print('Looking for a '+method + ' greater than ' + str(amount) +
          '. \nSieving with mats '+searchThru+' values.')

    startTime = time.time()
    for o in orders:
        sameTypeOrdersProfit = []
        for p in preped:
            if o[0]['type_id'] == p['type_id']:
                if 'mats_'+str(searchThru)+'_value' in p:
                    if method == "percentage" and p['mats_'+str(searchThru)+'_value'] > 0:
                        val = ((p['mats_'+str(searchThru)+'_value'] - o[0]['price'] * p['portion_size']) / p['mats_'+str(searchThru)+'_value']) * 100
                        if val > amount:
                            sameTypeOrdersProfit.append(o[0])
                    else:
                        val = p['mats_'+str(searchThru)+'_value'] - o[0]['price'] * p['portion_size']
                        if val > amount:
                            sameTypeOrdersProfit.append(o[0])
        if len(sameTypeOrdersProfit) > 0:
            goodStuff.append(sameTypeOrdersProfit)

    print('Done processing entries in --- %s ---' % (time.time() - startTime))
    print('Serving '+str(len(goodStuff))+' positions...')

    return goodStuff

