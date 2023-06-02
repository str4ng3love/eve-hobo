import asyncio
import requests
import json
from flask import Flask, request
from flask import render_template
from prisma import Prisma, register
from prisma.models import Item
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

@app.route('/hobo', methods=['GET', 'POST'])
def create():
    return '<p>new hobo awakens</p>'
   
        
 

