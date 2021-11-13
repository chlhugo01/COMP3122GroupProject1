from flask import Flask, jsonify, request, redirect, url_for, render_template
from pymongo import MongoClient
import pytest
import requests
import time
import os

app = Flask(__name__)
orderdb = MongoClient('mongodb://comp3122:23456@db2:27017')
restaurantdb = MongoClient('mongodb://comp3122:23456@db1:27017')

@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"Welcome Message": "Hello, order"}), 200

@app.route('/order', methods=['GET'])
def get_menu():
    rs = []
    for i in restaurantdb.Restaurant.restaurants.find({},{"_id": 0}).sort("id"):
        r = {'name': i['name'], 'address': i['address'], 'phone_number': int(i['phone_number'])}
        m = {}
        for j in restaurantdb.Restaurant.menu.find({},{"_id": 0}).sort("id"):
            if i['id'] == j['restaurant_id']:
                m[j['name']] = j['price']
        r['menu'] = m
        rs.append(r)
    return jsonify(rs), 200

@app.route('/order/<order_id>')
def order(order_id):
    # orderresult = orderdb.Order.order.find({"order_id":int(order_id)})
    # order = []
    # for i in orderresult:
    #     order.append({
    #         'customer_id': i["customer_id"],
    #         'restaurant_id':i["restaurant_id"],
    #         'delivery_id': i['delivery_id']
    #     })
    return jsonify(order), 200

@app.route('/testresult',methods=["GET"])
def testresult():
        a=pytest.main(['/app_order/unit.py']).value
        if(a == 0 ):
            return "ok",200
        else:
            return "not ok",400


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=15000)
