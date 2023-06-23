
from flask import Blueprint, jsonify, request
from globals import getState, setStateFalse, setStateTrue
from utils.helpers import timeSinceInput
from controllers.get_orders import get_pages
from controllers.get_records import get_orders_blob, get_TEL_buy_save, get_TEL_sell_save
from controllers.update_records import update_orders_blob
api = Blueprint('api', __name__)
globals()['isRunning'] = False


@api.route("/")
def showRoutes():
    routes = [
        {"name": "Eve-Hobo API v_0.1",
         "route": "https://eve-hobo.onrender.com/api",
         "description": "Displays current api routes."
         },
        {
            "name": "Update buy orders.",
            "description": "Updates buy orders DB to current ESI data. May take some time, can't run until 30 minutes passes since last update.",
            "route": "/esi-update-buy-orders",
        },
        {
            "name": "Update sell orders.",
            "description": "Updates sell orders DB to current ESI data. May take some time, can't run until 30 minutes passes since last update.",
            "route": "/esi-update-sell-orders",
        },
        {
            "name": "Get buy orders.",
            "description": "Displays buy orders contained in DB. JSON format.",
            "route": "/get-buy-orders",
        },
        {
            "name": "Get sell orders.",
            "description": "Displays sell orders contained in DB. JSON format.",
            "route": "/get-sell-orders",
        },
        {
            "name": "Time elapsed since last buy orders update.",
            "description": "Check when last buy orders update was completed.",
            "route": "/check-last-buy-save",
        },
        {
            "name": "Time elapsed since last sell orders update.",
            "description": "Check when last sell orders update was completed.",
            "route": "/check-last-sell-save",
        },
    ]
    return jsonify(routes)


@api.route('/esi-update-buy-orders', methods=['GET', 'POST'])
def updateBuyOrders():
    if request.method == 'GET':
        isRunning = getState()
        if isRunning == True:
            return "DB is updating, please wait..."
        else:
            setStateTrue()
            limit = 30
            time = get_TEL_buy_save()
            if "DB" in time:
                buyOrders = get_pages("buy")
                result = update_orders_blob(buyOrders, "buy_orders")
                setStateFalse()
                return result
            else:
                timediff = timeSinceInput(time, limit)
                if timediff['evaluation'] == False:
                    setStateFalse()
                    return jsonify("Too early to update, "+str(limit)+" minutes must pass since last update. Last update was "+timediff['time'] + ' ago.')
                else:
                    buyOrders = get_pages("buy")
                    result = update_orders_blob(buyOrders, "buy_orders")
                    setStateFalse()
                    return result

    else:
        return "Bad request!", 401


@api.route('/esi-update-sell-orders', methods=['GET', 'POST'])
def updateSellOrders():
    if request.method == 'GET':
        isRunning = getState()
        if isRunning == True:
            return "DB is updating, please wait..."
        else:
            setStateTrue()
            limit = 30
            time = get_TEL_sell_save()
            if "DB" in time:
                sellOrders = get_pages("sell")
                result = update_orders_blob(sellOrders, "sell_orders")
                setStateFalse()
                return result
            else:
                timediff = timeSinceInput(time, limit)
                if timediff['evaluation'] == False:
                    setStateFalse()
                    return jsonify("Too early to update, "+str(limit)+" minutes must pass since last update. Last update was "+timediff['time'] + ' ago.')
                else:
                    sellOrders = get_pages("sell")
                    result = update_orders_blob(sellOrders, "sell_orders")
                    setStateFalse()
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
    return jsonify("Buy orders last updated: "+time)


@api.route('/check-last-sell-save')
def TELSellUpdate():
    time = get_TEL_sell_save()
    return jsonify("Sell orders last updated: "+time)
