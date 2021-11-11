from flask import request, Flask, jsonify
from pymongo import MongoClient, errors
import sys

app = Flask(__name__)
myclient = MongoClient('mongodb://comp3122:23456@db1:27017')
mydb = myclient['Order']
myorder = mydb['order']

parameter_error_message = {"error": "parameter not found!"}
error_message = {"error": "not found!"} 

@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"Hello": "World!"}), 200

@app.route('/view/<order_id>', methods=['GET'])
def view(order_id):
    obj = myorder.find_one({'order_id' : int(order_id)}, {"_id": 0})
    if obj is None:
        return jsonify(error_message), 404
    return jsonify(obj), 200

@app.route('/order', methods=['POST'])
def order():
    if 'foodnumber' in request.args.keys():
        foodnumber = int(request.args['foodnumber'])
    else:
        return jsonify(parameter_error_message), 404
    food = []
    for i in range(foodnumber):
        f = 'fid'+str(i)
        q = 'fq'+str(i)
        if f in request.args.keys() and q in request.args.keys():
            x = {int(request.args[f]): int(request.args[q])}
            food.append(x)
        else:
            return jsonify(parameter_error_message), 404
    return jsonify(food), 200
# start flask server
if __name__ == '__main__':
    with MongoClient('mongodb://comp3122:23456@db1:27017') as client:     # Test connect string
        try:                                                # 
            client.admin.command('ismaster')                  # `ismaster` command is cheap
        except errors.ServerSelectionTimeoutError:  # Timeout when cannot find the db with hostname and port
            sys.exit('Connection refused. Please check the hostname and the port number of mongodb.')
        except errors.OperationFailure as err:      # Authentication failure is part of `OperationFailure`
            if err.code == 18:                                # code 18 == autnehtication failure
                sys.exit('Authentication failed. Please check the username and password.')
            else:                                             #
             sys.exit(err)                                   # print other errors and exit
        except errors.PyMongoError as err:          
            sys.exit(err)
    app.run(host='0.0.0.0', debug=True, port=15000)