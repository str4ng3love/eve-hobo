from flask import Blueprint, jsonify
from controllers.get_records import getMaterials, getMaterialByTypeId, getMaterialsByString, getMatsBuyPrice, getMatsSellPrice
mats = Blueprint('materials', __name__)


@mats.route("/")
def getMats():

    return jsonify(getMaterials())


@mats.route("/<name>")
def getMatsName(name):

    return jsonify(getMaterialsByString(name))


@mats.route("/type/<type_id>")
def getMatsTypeId(type_id):

    return jsonify(getMaterialByTypeId(type_id))

@mats.route("/buy-price")
def getMatsBuyPriceList():
    prices = getMatsBuyPrice()
    return jsonify(prices)

@mats.route("/sell-price")
def getMatsSellPriceList():
    prices = getMatsSellPrice()
    return jsonify(prices)