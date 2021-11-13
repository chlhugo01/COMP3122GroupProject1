from flask import Flask, jsonify, request, redirect, url_for, render_template
from pymongo import MongoClient
import pytest
import requests
import time
import os

app = Flask(__name__)
client = MongoClient('mongodb://comp3122:23456@db1:27017')

@app.route('/')
def todo():
    return jsonify({"Student ID": "190dfdsfd7d", "Name": "Lee Chun Hang"}), 200

@app.route('/store')
def me():
    return render_template('store.html', storearr=temp6)

@app.route('/resturant/<resturant_id>')
def store_name(resturant_id):
    menuresult = client.Menu.menu.find({"restaurant_id":int(resturant_id)})
    menu = []
    for food in menuresult:
        menu.append({
            'Food_Name': food["Food_Name"],
            'Food_id':food["Food_id"],
            'Food_Price': food['Food_Price']
        })
    return render_template('menu.html',menu=menu)

@app.route('/testresult',methods=["GET"])
def testresult():
        a=pytest.main(['/app_restaurant/unit.py']).value
        if(a == 0 ):
            return "ok",200
        else:
            return "not ok",400


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=15000)
