from flask import request, Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
orderdb = MongoClient('mongodb://comp3122:23456@db2:27017').order

@app.route('/view', methods=['GET'])
def food_pos():
    return jsonify(), 200

@app.route('/take/<receipt_id>', methods=['GET'])
def take_food(receipt_id):
    return jsonify(), 200

@app.route('/delivered/<receipt_id>', methods=['GET'])
def food_arrived(receipt_id):
    return jsonify(), 200

# start flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=15105)