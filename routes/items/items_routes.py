from flask import Blueprint, jsonify
from controllers.get_records import getItemsList, getItemsByString, getItemByTypeId
items = Blueprint('items', __name__)


@items.route("/")
def getItems():

    return jsonify(getItemsList())


@items.route("/<name>")
def getItemsTypeId(name):

    return jsonify(getItemsByString(name))


@items.route("/type/<type_id>")
def getItemsName(type_id):

    return jsonify(getItemByTypeId(type_id))
