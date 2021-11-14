from flask import Flask, jsonify, request, redirect, url_for, render_template, session
from pymongo import MongoClient
import jwt
import pytest
import requests
import datetime
import time
import os
import redis
import json

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379)

client = MongoClient('mongodb://comp3122:23456@db0:27017')

def authenticate_token(token):
    return jwt.decode(token, "secretPassword", algorithms=["HS256"])


@app.route('/')
def todo():
    return jsonify({"Message": "Welcome to login page"}), 200


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        r = requests.post('http://localhost:15000/api/login?username='+username+'&password='+password)
        data = r.json()
        session['token'] = data['token']
        return data
    else:
        return render_template('login.html')


@app.route('/api/login', methods=['POST'])
def api_login():
    username = request.args.get('username')
    password = request.args.get('password')
    if result := client.user.customer.find_one({"username": username,'password':password}):
        id = result['customer_id']
        payload = {'id': id, 'usergroup': 'customer', 'logindt': str(datetime.datetime.utcnow())}
    elif result := client.user.restaurant.find_one({"username": username,'password':password}):
        id = result['restaurant_id']
        payload = {'id': id, 'usergroup': 'customer', 'logindt': str(datetime.datetime.utcnow())}
    elif result := client.user.delivery.find_one({"username": username,'password':password}):
        id = result['restaurant_id']
        payload = {'id': id, 'usergroup': 'customer', 'logindt': str(datetime.datetime.utcnow())}
    else:
        return {'error': 'user not found'}, 404
    token = jwt.encode(payload, "secretPassword", algorithm="HS256")
    session['token'] = token
    return {'token': token}, 200


@app.route('/api/order/<int:r>', methods=['POST'])
def api_order(r):
    token = request.args.get('token')
    load = authenticate_token(token)
    orders = []
    count = 0
    while True:
        f, q = 'food_id'+str(count), 'quantity'+str(count)
        if f in request.args.keys() and q in request.args.keys():
            orders.append({'id': request.args.get(f), 'quantity': request.args.get(q)})
        else:
            break
        count+=1
    data = {'user_id': load['id'], 'restaurant_id': r, 'orders': orders}
    jsonstr = json.dumps(data)

    r.publish('customer_order', jsonstr)
    

    return jsonstr



@app.route('/testresult',methods=["GET"])
def testresult():
        a=pytest.main(['/app_login/unit.py']).value
        if(a == 0 ):
            return "ok",200
        else:
            return "not ok",400

if __name__ == "__main__":
    app.secret_key = 'secret_key'
    app.run(host='0.0.0.0', debug=True, port=15000)

