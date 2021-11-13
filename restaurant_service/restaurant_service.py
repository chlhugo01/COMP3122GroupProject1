from flask import Flask, jsonify, request, redirect, url_for, render_template
from pymongo import MongoClient
import pytest
import requests
import time
import os

app = Flask(__name__)
orderdb = MongoClient('mongodb://comp3122:23456@db2:27017').order
menuCollection = MongoClient('mongodb://comp3122:23456@db1:27017').Restaurant.menu
@app.route('/')
def welcome():
    return jsonify({"Welcome Message": "Hello, Restaurant"}), 200

@app.route('/restaurant/<resturant_id>', methods=['GET'])
def prepare_food(resturant_id):
    todo = []
    for i in orderdb.receipts.find({'restaurant_id': int(resturant_id), 'status': 'ordered'},{'_id': 0}):
        list = []
        list.append({'customer_id': int(i['customer_id']),
                        'receipt_id': int(i['id'])})
        food = {}
        for j in orderdb.details.find({'receipt_id': i['id']}, {'_id': 0}):
            f_name = menuCollection.find_one({'id': j['food_id']})['name']
            food[f_name] = int(j['number'])
        list.append(food)
        todo.append(list)
    return jsonify(todo), 200

@app.route('/done/<receipt_id>', methods=['GET'])
def complete_food(receipt_id):
    x = orderdb.receipts.find_one({'id': int(receipt_id), 'status': 'ordered'},{'_id': 0})
    if x is None:
        return jsonify({'error': 'receipt not found or it is already completed.'}), 404
    orderdb.receipts.update_one({'id': int(receipt_id)}, { "$set": {'status': 'done'}})
    x = orderdb.receipts.find_one({'id': int(receipt_id)},{'_id': 0})
    return jsonify(x), 200

@app.route('/testresult',methods=["GET"])
def testresult():
        a=pytest.main(['/app_restaurant/unit.py']).value
        if(a == 0 ):
            return "ok",200
        else:
            return "not ok",400


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=15000)
