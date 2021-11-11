from flask import request, Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
myclient = MongoClient('mongodb://comp3122:23456@mongo:27107')

# start flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15107)