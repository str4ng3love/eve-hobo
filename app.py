from flask import Flask
from flask import render_template
import requests
import json
app = Flask(__name__)

@app.route("/")
def index():
 
 
    return render_template('index.html')

@app.route('/about')
def about():

    return render_template('about.html')
@app.route('/salvager')
def salvager():

    return render_template('salvage.html')