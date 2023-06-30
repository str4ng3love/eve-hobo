
from flask import Blueprint, jsonify, request
from globals import getState, setStateFalse, setStateTrue
from utils.helpers import timeSinceInput
from routes.items.items_routes import items
from routes.materials.material_routes import mats
from controllers.get_orders import getPages
from controllers.get_records import getOrdersBlob, getTELBuySave, getTELSellSave
from controllers.update_records import updateOrdersBlob
api = Blueprint('api', __name__)
api.register_blueprint(items, url_prefix="/items")
api.register_blueprint(mats, url_prefix="/materials")



@api.route("/")
def showRoutes():
    routes = {
        "name": "Eve-Hobo API v_0.1",
        "roo-route": "https://eve-hobo.onrender.com/api",
        "description": "Displays current api routes. Usage: root-route + route. For instance: to get information on the Enyo by type_id, hit https://eve-hobo.onrender.com/api/items/type/12044",

        "routes": [
             {
                "name": "Update buy orders.",
                 "description": "Updates buy orders DB to current ESI data. May take some time, can't run until 30 minutes have passed since last update.",
                 "route": "/esi-update-buy-orders",
             },
            {
                 "name": "Update sell orders.",
                "description": "Updates sell orders DB to current ESI data. May take some time, can't run until 30 minutes have passed since last update.",
                "route": "/esi-update-sell-orders",
             },
            {
                 "name": "Get buy orders.",
                "description": "Displays buy orders contained in DB. JSON format.",
                "route": "/buy-orders",
             },
            {
                 "name": "Get sell orders.",
                "description": "Displays sell orders contained in DB. JSON format.",
                "route": "/sell-orders",
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
            {
                 "name": "Get materials.",
                "description": "Displays materials used in industry.",
                "route": "/materials",
             },
            {
                 "name": "Get materials by name.",
                "description": "Takes a string:str(case insensitive) and returns a list of materials that contain string:str in their names.",
                "route": "/materials/<name>",
             },
            {
                 "name": "Get material by type_id.",
                "description": "Takes material's type_id:int and returns material.",
                "route": "/materials/type/<type_id>",
             },
            {
                 "name": "Get items.",
                "description": "Displays items used in industry.",
                "route": "/items",
             },
              {
                 "name": "Get reprocessable items.",
                "description": "Displays items used in industry that can be reprocessed.",
                "route": "/items/reprocessable",
             },
            {
                 "name": "Get items by name.",
                "description": "Takes a string:str(case insensitive) and returns a list of items that contain string:str in their names.",
                "route": "/items/<name>",
             },
            {
                 "name": "Get item by type_id.",
                "description": "Takes item's type_id:int and returns an item.",
                "route": "/items/type/<type_id>",
             }
        ]



    }
    return jsonify(routes)


@api.route('/esi-update-buy-orders', methods=['GET', 'POST'])
def updateBuyOrders():
    if request.method == 'GET':
        isRunning = getState()
        if isRunning == True:
            return {"message":"DB is updating, please wait..."}
        else:
            setStateTrue()
            limit = 30
            time = getTELBuySave()
            if "DB" in time:
                buyOrders = getPages("buy")
                result = updateOrdersBlob(buyOrders, "buy_orders")
                setStateFalse()
                return jsonify(result)
            else:
                timediff = timeSinceInput(time, limit)
                if timediff['evaluation'] == False:
                    setStateFalse()
                    return jsonify({"error":"Too early to update, "+str(limit)+" minutes must pass since last update. Last update was "+timediff['time'] + ' ago.'})
                else:
                    buyOrders = getPages("buy")
                    result = updateOrdersBlob(buyOrders, "buy_orders")
                    setStateFalse()
                    return jsonify(result)

    else:
        return "Bad request!", 401


@api.route('/esi-update-sell-orders', methods=['GET', 'POST'])
def updateSellOrders():
    if request.method == 'GET':
        isRunning = getState()
        if isRunning == True:
            return {"message":"DB is updating, please wait..."}
        else:
            setStateTrue()
            limit = 30
            time = getTELSellSave()
            if "DB" in time:
                sellOrders = getPages("sell")
                result = updateOrdersBlob(sellOrders, "sell_orders")
                setStateFalse()
                return result
            else:
                timediff = timeSinceInput(time, limit)
                if timediff['evaluation'] == False:
                    setStateFalse()
                    return jsonify({"error":"Too early to update, "+str(limit)+" minutes must pass since last update. Last update was "+timediff['time'] + ' ago.'})
                else:
                    sellOrders = getPages("sell")
                    result = updateOrdersBlob(sellOrders, "sell_orders")
                    setStateFalse()
                    return result
    else:
        return "Bad request!", 401


@api.route('/buy-orders', methods=['GET', 'POST'])
def getBuyOrders():
    if request.method == 'GET':
        return getOrdersBlob("buy_orders")
    else:
        return "Bad request!", 401


@api.route('/sell-orders', methods=['GET', 'POST'])
def getSellOrders():
    if request.method == 'GET':
        return getOrdersBlob("sell_orders")
    else:
        return "Bad request!", 401


@api.route('/check-last-buy-save')
def TELBuyUpdate():
    time = getTELBuySave()
    return jsonify("Buy orders last updated: "+time)


@api.route('/check-last-sell-save')
def TELSellUpdate():
    time = getTELSellSave()
    return jsonify("Sell orders last updated: "+time)
