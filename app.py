from globals import getState, setStateTrue
from controllers.get_records import get_orders_blob, get_TEL_sell_save, get_TEL_buy_save
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
    TELBuyUpdate =  get_TEL_buy_save()
    TELLSellUpdate = get_TEL_sell_save()
    
    return render_template('salvage.html', title='Eve Hobo | Salvager',TELBuyUpdate= TELBuyUpdate, TELLSellUpdate=TELLSellUpdate )


@app.route('/buy_orders')
def buy_orders():

    return render_template('buy_orders.html', title='Eve Hobo | Buy Orders')



# testing
