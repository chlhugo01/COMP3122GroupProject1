from flask import Flask, jsonify, request, redirect, url_for, render_template
from pymongo import MongoClient
import pytest
import requests
import time
import os

app = Flask(__name__)
client = MongoClient('mongodb://comp3122:23456@db2:27017')

@app.route('/')
def todo():
    return jsonify({"Student ID": "190dfdsfd7d", "Name": "Lee Chun Hang"}), 200

@app.route('/Order/<order_id>')
def store_name(order_id):
    orderresult = client.Order.order.find({"order_id":int(order_id)})
    order = []
    for i in orderresult:
        order.append({
            'customer_id': i["customer_id"],
            'restaurant_id':i["restaurant_id"],
            'delivery_id': i['delivery_id']
        })
    return jsonify(order),200


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=15000)
