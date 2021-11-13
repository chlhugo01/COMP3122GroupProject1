from flask import Flask, jsonify, request, redirect, url_for, render_template
from pymongo import MongoClient
import pytest
import requests
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
        customerresult = client.user.customer.find_one({"username": username,'password':password})
        restaurantresult = client.user.restaurant.find_one({"username": username,'password':password})
        deliveryresult = client.user.delivery.find_one({"username": username,'password':password})
        if customerresult:
            return "Customer "+username+password
        elif restaurantresult:
            return "restaurant "+username+password
        elif deliveryresult:
            return "delivery "+username+password
        else:
            return "NO account info"
    else:
        return render_template('login.html')



@app.route('/testresult',methods=["GET"])
def testresult():
        a=pytest.main(['/app_login/unit.py']).value
        if(a == 0 ):
            return "ok",200
        else:
            return "not ok",400

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=15000)

