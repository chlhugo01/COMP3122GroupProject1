from flask import request, Flask, jsonify
import pymongo
import sys

app = Flask(__name__)
client = pymongo.MongoClient('mongodb://comp3122:23456@db1:27017')

db = client["Restaurant"] 
restaurant= db["restaurants"] 
menu = db["menu"]

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'Message': 'Hello i am running'}), 200

@app.route('/addmenu/<restaurantId>/<name>/<Price>', methods=['GET'])
def addmenu(restaurantId,name,Price):
    restaurant_id = int(restaurantId)
    price = int(Price)
    lastid = menu.find_one({},{"_id":0,"id":1},sort=[("id",-1)])['id']
    store = menu.find({"restaurant_id":restaurant_id},{"_id":0})
    if store is not None:
        samefood = menu.find_one({"restaurant_id":restaurant_id,"name":name},{"_id":0})
        if samefood is not None:
            return jsonify({'Message': 'This food is already in the menu'}),200
        else:
            menu.insert_one({'id':lastid+1,'restaurant_id':restaurant_id,'name':name,'price':price})
            check = menu.find_one({'id':lastid+1},{"_id":0})
            if check is not None:
                return jsonify({'Message': 'This food has added into the menu'}), 201
            else:
                return jsonify({'Message': 'error cannot add'}), 404
    else:
        return jsonify({'Message': 'Does not have this restaurant'}),200

@app.route('/deletemenu/<restaurantId>/<name>', methods=['GET'])
def deletemenu(restaurantId,name):
    restaurant_id = int(restaurantId)
    store = menu.find_one({"restaurant_id":restaurant_id},{"_id":0})
    if store is not None:
        samefood = menu.find_one({"restaurant_id":restaurant_id,"name":name},{"_id":0})
        if samefood is not None:
            myquery = {"restaurant_id":restaurant_id,"name":name}
            menu.delete_one(myquery)
            return jsonify({'Message': 'This food has deleted in the menu'}),200
        else:
            return jsonify({'Message': 'No such food in the menu'}), 200
    else:
        return jsonify({'Message': 'Does not have this restaurant'}),200

@app.route('/editmenu/<id>/<name>/<price>', methods=['GET'])
def editmenu(id,name,price):
    intid = int(id)
    checkid = menu.find_one({"id":intid},{"_id":0})
    if checkid is not None:
        oldname = menu.find_one({"id":intid},{"_id":0})['name']
        oldprice = menu.find_one({"id":intid},{"_id":0})['price']
        myquery = { "name": oldname, "price": oldprice }
        newvalues = { "$set": { "name": name, "price": price } }
        menu.update_one(myquery, newvalues)
        return jsonify({'Message': 'Edit success'}),200
    else:
        return jsonify({'Message': 'Does not have this id'}),200

@app.route('/menu', methods=['GET'])
def showmenu():
    show = menu.find({},{"_id":0}).sort("id") 
    output = []
    for x in show:
        output.append(x)
    return jsonify(output),200

# start flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, port=15000)