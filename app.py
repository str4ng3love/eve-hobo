import asyncio
import requests
import json
from flask import Flask, request
from flask import render_template
from prisma import Prisma, register
from prisma.models import Item
app = Flask(__name__)
prisma = Prisma()
from prisma.models import Item

db = Prisma(auto_register=True)
async def main() -> None:
    await db.connect()

    item = await Item.prisma().create(
        data={
            'name':'zenon',
            'typeId':12038
        }
    )
    await db.disconnect()

    
@app.route("/")

def index():
    # asyncio.run(main())
    title = 'Eve Hobo'
    return render_template('layout.html', title=title)

@app.route('/about')
def about():

    return render_template('/about.html', title='Eve HObo | About')
@app.route('/salvager')
def salvager():

    return render_template('salvage.html', title='Eve HObo | Salvager')

@app.route('/hobo', methods=['GET', 'POST'])
def create():
    return '<p>new hobo awakens</p>'
   
        
 

