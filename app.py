from flask import Flask
from flask import render_template
import requests
import json
from types import SimpleNamespace
app = Flask(__name__)

@app.route("/")
def index():
    tritSell = requests.get('https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=34')
    cenaTrit = json.loads(tritSell.text)
    print(cenaTrit)
    return render_template('index.html')