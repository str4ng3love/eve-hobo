
from controllers.get_orders import  get_buy_orders, get_sell_orders, get1pageBuy
from controllers.update_records import update_buy_orders
from controllers.get_records import get_orders
from flask import Flask, request, jsonify
from flask import render_template
app = Flask(__name__)


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

   

@app.route('/api/get-buy-orders', methods=['GET', 'POST'])
def getBuyOrders():
    buyOrders =  get_buy_orders()
    result = update_buy_orders(buyOrders)
    return jsonify(result)

@app.route('/api/get-sell-orders', methods=['GET', 'POST'])
def getSellOrders():
    sellOrders =  get_sell_orders()
    return jsonify(sellOrders)

@app.route('/api/test/get-buy-and-filter')
def main():
    orders = get1pageBuy()

    return jsonify(orders)
@app.route('/api/get-orders', methods=['GET', 'POST'])
def getOrders():
    
    results = get_orders()
    
    return results
