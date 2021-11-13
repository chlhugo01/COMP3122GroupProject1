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

@app.route('/menu', methods=['GET'])
def get_menu():
    rs = []
    for i in restaurantdb.Restaurant.restaurants.find({},{"_id": 0}).sort("id"):
        r = {'name': i['name'], 'address': i['address'], 'phone_number': int(i['phone_number'])}
        m = {}
        for j in restaurantdb.Restaurant.menu.find({},{"_id": 0}).sort("id"):
            if i['id'] == j['restaurant_id']:
                m[str(int(j['id'])) + ": " + j['name']] = j['price']
        r['menu'] = m
        rs.append(r)
    return jsonify(rs), 200

@app.route('/order/<int:r>', methods=['GET'])
def order(r):
    foods = []
    food_count = 0
    total = 0
    while True:
        f = 'fid'+str(food_count)
        q = 'fq'+str(food_count)
        if f in request.args.keys() and q in request.args.keys():
            id = int(request.args[f])
            n = int(request.args[q])
            x = restaurantdb.Restaurant.menu.find_one({'id': id, 'restaurant_id': r}, {'_id': 0})
            if x is not None:
                foods.append([x['id'], n, x['price']])
                total += n * x['price']
                food_count += 1
            else:
                return jsonify({'error': 'restaurant ' + r + ' not found food ' + id}), 404
        elif food_count > 0:
            result = []
            new_receipt = {}
            receipts_max_id = orderdb.order.receipts.find_one({}, {'_id': 0}, sort=[('id', -1)])['id']
            new_receipt["id"] = int(receipts_max_id + 1)
            new_receipt["customer_id"] = int(0)  # This is hardcode, need to change after the pubsub is finished.
            new_receipt["restaurant_id"] = r
            new_receipt["status"] = 'ordered'
            orderdb.order.receipts.insert_one(new_receipt)
            new_receipt = orderdb.order.receipts.find_one({'id' : receipts_max_id + 1}, {"_id": 0})
            result.append(new_receipt)
            # db.details.insertOne({'id': 1, 'receipts_id': 1, 'food_id': 1, 'number': 1, 'total_price': 5});
            foodlist = []
            details_max_id = orderdb.order.details.find_one({}, {'_id': 0}, sort=[('id', -1)])['id']
            for food in foods:
                detail = {}
                detail["id"] = int(details_max_id + 1)
                detail["receipt_id"] = int(new_receipt['id'])
                detail["food_id"] = int(food[0])
                detail["number"] = food[1]
                detail["price"] = food[2]
                orderdb.order.details.insert_one(detail)
                detail = orderdb.order.details.find_one({'id' : details_max_id + 1}, {"_id": 0})
                foodlist.append(detail)
                details_max_id += 1
            result.append(foodlist)
            result.append({'total': total})
            return jsonify(result), 200
        return jsonify({'error': 'parameter empty'}), 404

@app.route('/testresult',methods=["GET"])
def testresult():
        a=pytest.main(['/app_order/unit.py']).value
        if(a == 0 ):
            return "ok",200
        else:
            return "not ok",400


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=15000)
