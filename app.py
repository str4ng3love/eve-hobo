import asyncio
import requests
import json
from controllers.get_orders import  get_buy_orders, get_sell_orders
from flask import Flask, request, jsonify
from flask import render_template
from prisma import Prisma, register
from prisma.models import Item
app = Flask(__name__)
prisma = Prisma()
from prisma.models import Item

@app.route("/")
def index():
    title = 'Eve Hobo'
    return render_template('layout.html', title=title)

@app.route('/about')
def about():

    return render_template('/about.html', title='Eve Hobo | About')
@app.route('/salvager')
def salvager():

    return render_template('salvage.html', title='Eve Hobo | Salvager')

   

@app.route('/api/get-buy-prices', methods=['GET', 'POST'])
def getBuyOrders():
    buyOrders =  get_buy_orders()
    return jsonify(buyOrders)

@app.route('/api/get-sell-prices', methods=['GET', 'POST'])
def getSellOrders():
    sellOrders =  get_sell_orders()
    return jsonify(sellOrders)
