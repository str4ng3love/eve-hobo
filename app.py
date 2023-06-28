
from controllers.get_records import getTELSellSave, getTELBuySave, getItemsReprocessable, getOrdersBlob
from controllers.handleRequests import get_filtered_and_sorted_orders
from routes.api_routes import api
from flask import Flask, jsonify, request
from flask import render_template
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


@app.route('/reprocess-buy',  methods=["GET", "POST"])
def reprocess_buy():
    if request.method == "POST":
        baseReprocessReturn = 0.5
        searchBy = request.form['search-by']
        amount = request.form['amount']

        orders = get_filtered_and_sorted_orders('buy_orders')

        return jsonify(orders)
    else:
        return jsonify({'error': 'Bad request.'}, 400)


@app.route('/reprocess-sell',  methods=["GET", "POST"])
def reprocess_sell():
    if request.method == "POST":
        searchBy = request.form['search-by']
        amount = request.form['amount']
        orders = get_filtered_and_sorted_orders('buy_orders')

        return jsonify(orders)
    else:
        return jsonify({'error': 'Bad request.'}, 400)


# @app.route('/repro')
# def reprocess():


#     return jsonify(reprocessed)

# # testing
