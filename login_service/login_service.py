from flask import Flask, jsonify, request, redirect, url_for, render_template, session
from pymongo import MongoClient
import jwt
import pytest
import requests
import datetime
import time
import os

app = Flask(__name__)

client = MongoClient('mongodb://comp3122:23456@db0:27017')

@app.route('/')
def todo():
    return jsonify({"Student ID": "190dfd", "Name": "Lee Chun Hang"}), 200


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
    if client.user.customer.find_one({"username": username,'password':password}):
            payload = {'username': username, 'usergroup': 'customer', 'logindt': str(datetime.datetime.utcnow())}
    elif client.user.restaurant.find_one({"username": username,'password':password}):
        return "restaurant "+username+password
    elif client.user.delivery.find_one({"username": username,'password':password}):
        return "delivery "+username+password
    else:
        return "NO account info"
    token = jwt.encode(payload, "secret", algorithm="HS256")
    session['token'] = token
    return {'token': token}




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

