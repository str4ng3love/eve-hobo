

from controllers.get_records import get_orders_blob
from routes.api_routes import api
from flask import Flask, jsonify
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

    return render_template('salvage.html', title='Eve Hobo | Salvager')


@app.route('/buy_orders')
def buy_orders():

    return render_template('buy_orders.html', title='Eve Hobo | Buy Orders')



# testing

@app.route('/test/blob-read')
def testingBlobRead():

    buyOrdersBlob = get_orders_blob("buy_orders")
    return jsonify(buyOrdersBlob)
