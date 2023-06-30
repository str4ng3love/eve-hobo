
from controllers.get_records import getTELSellSave, getTELBuySave, getItemsReprocessable, getOrdersBlob, getMatsBuyPrice, getMatsSellPrice
from controllers.utilities import get_filtered_and_sorted_orders, prepareItems
from controllers.process_data import findDealsByMethod
from routes.api_routes import api
from flask import Flask, jsonify, request
from flask import render_template
import time
app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')


@app.route("/")
def index():
    title = 'Eve Hobo'
    return render_template('layout.html', title=title)


@app.route('/about')
def about():

    return render_template('about.html', title='Eve Hobo | About')


@app.route('/salvager')
def salvager():
    TELBuyUpdate = getTELBuySave()
    TELLSellUpdate = getTELSellSave()

    return render_template('salvage.html', title='Eve Hobo | Salvager', TELBuyUpdate=TELBuyUpdate, TELLSellUpdate=TELLSellUpdate)


# @app.route('/reprocess-buy',  methods=["GET", "POST"])
# def reprocess_buy():
#     if request.method == "POST":
#         searchMethod = request.form['search-by']
#         amount = request.form['amount']
#         orders = findDealsByMethod(searchMethod, int(amount), 0)
#         return jsonify(orders)
#     else:
#         return jsonify({'error': 'Bad request.'}, 400)


# @app.route('/reprocess-sell',  methods=["GET", "POST"])
# def reprocess_sell():
#     if request.method == "POST":
#         searchBy = request.form['search-by']
#         amount = request.form['amount']
#         orders = get_filtered_and_sorted_orders('sell_orders')

#         return jsonify(orders)
#     else:
#         return jsonify({'error': 'Bad request.'}, 400)


# @app.route('/repro')
# def reprocess():


#     return jsonify(reprocessed)

# # testing
@app.route('/test-get')
def tes2t():
 

    goodStuff = findDealsByMethod('sell_orders' ,'percentage', 0, 'sell')
    return jsonify(goodStuff)


# todo: frontend ui and possibly front end calculations