db.auth('comp3122', '23456')
db = db.getSiblingDB('Order')

db.createCollection('order');

db.order.insertOne({'order_id':00001, 'customer_id':1,'store_id':1,'delivery_id':1});
db.order.insertOne({'order_id':00002, 'customer_id':2,'store_id':1,'delivery_id':2});
db.order.insertOne({'order_id':00003, 'customer_id':2,'store_id':3,'delivery_id':3});


db.createCollection('detail');
db.detail.insertOne({'order_id': 00001, 'food_id': 1, 'number':1});
db.detail.insertOne({'order_id': 00001, 'food_id': 2, 'number':2});
db.detail.insertOne({'order_id': 00002, 'food_id': 1, 'number':2});
db.detail.insertOne({'order_id': 00003, 'food_id': 1, 'number':1});