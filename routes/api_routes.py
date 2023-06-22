from flask import Blueprint, jsonify, request
from controllers.get_orders import get_pages
from controllers.get_records import get_orders_blob, get_TEL_buy_save, get_TEL_sell_save
from controllers.update_records import update_orders_blob
api = Blueprint('api', __name__)


@api.route('/esi-update-buy-orders', methods=['GET', 'POST'])
def updateBuyOrders():
    if request.method == 'GET':
        buyOrders = get_pages()
        result = update_orders_blob(buyOrders, "buy_orders")

        return result
    else:
        return "Bad request!", 401


@api.route('/esi-update-sell-orders', methods=['GET', 'POST'])
def updateSellOrders():
    if request.method == 'GET':
        sellOrders = get_pages()
        result = update_orders_blob(sellOrders, "sell_orders")

        return result
    else:
        return "Bad request!", 401


@api.route('/get-buy-orders', methods=['GET', 'POST'])
def getBuyOrders():
    if request.method == 'GET':
        return get_orders_blob("buy_orders")
    else:
        return "Bad request!", 401


@api.route('/get-sell-orders', methods=['GET', 'POST'])
def getSellOrders():
    if request.method == 'GET':
        return get_orders_blob("sell_orders")
    else:
        return "Bad request!", 401

@api.route('/check-last-buy-save')
def TELBuyUpdate():
    time = get_TEL_buy_save()
    return "Buy orders last updated: "+time
@api.route('/check-last-sell-save')
def TELSellUpdate():
    time = get_TEL_sell_save()
    return "Sell orders last updated: "+time