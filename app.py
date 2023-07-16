
from controllers.get_records import getTELSellSave, getTELBuySave

from routes.api_routes import api
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')


@app.route("/")
def index():
    title = 'Eve Hobo'
    TELBuyUpdate = getTELBuySave()
    TELLSellUpdate = getTELSellSave()

    return render_template('base.html', title=title, TELBuyUpdate=TELBuyUpdate, TELLSellUpdate=TELLSellUpdate)


@app.route('/about')
def about():

    return render_template('about.html', title='Eve Hobo | About')


@app.route('/salvager')
def salvager():

    return render_template('salvage.html', title='Eve Hobo | Salvager')



# todo: frontend ui and possibly front end calculations