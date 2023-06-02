from flask import Flask
from flask import render_template
import requests
import json
app = Flask(__name__)

@app.route("/")
def index():
    tritSell = requests.get('https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=34')
    headers = tritSell.headers
    
    # cenaTrit = json.loads(tritSell.text)
    # print(cenaTrit[2]["price"])
    return render_template('index.html')

@app.route('/about')
def about():

    return render_template('about.html')
@app.route('/salvager')
def salvager():

    return render_template('salvage.html')