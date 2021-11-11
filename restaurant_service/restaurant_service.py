from flask import Flask, jsonify, request, redirect, url_for, render_template
from pymongo import MongoClient
import pytest
import requests
import time
import os

app = Flask(__name__)
client = MongoClient('mongodb://comp3122:23456@mongo:27104')
store = client.Order.Store.find()
storearr = []
for doc in store:
    storearr.append(doc)
temp6 = []
for user in storearr:
    temp6.append({
        'id': int(user["id"]),
        'name': user["name"],
        'address': user["address"],
        # 'gpa' : user["gpa"]
    })


@app.route('/')
def todo():
    return jsonify({"Student ID": "190dfdsfd7d", "Name": "Lee Chun Hang"}), 200


@app.route('/store')
def me():
    #return jsonify(menuarray),200
    return render_template('store.html', storearr=temp6)


@app.route('/store/<store_id>')
def store_name(store_id):
    menuresult = client.Order.FoodMenu.find({"store_id": int(store_id)})
    menuarray=[]
    for i in menuresult:
        menuarray.append({
        'store_id': i["store_id"],
        'food_id': i["food_id"],
        'food_name': i["food_name"],
        'food_nrice': i["food_price"]
        })
    #return jsonify(menuarray),200
    return render_template('menu.html', menu=menuarray)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=15000)
