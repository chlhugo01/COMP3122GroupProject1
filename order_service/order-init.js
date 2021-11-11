db.auth('comp3122', '23456')
db = db.getSiblingDB('Order')

db.createCollection('order');

db.order.insertOne({'order_id': 1, 'customer_id': 1,'store_id': 1,'delivery_id': 1});
db.order.insertOne({'order_id': 2, 'customer_id': 2,'store_id': 1,'delivery_id': 2});
db.order.insertOne({'order_id': 3, 'customer_id': 2,'store_id': 3,'delivery_id': 3});


db.createCollection('detail');
db.detail.insertOne({'order_id': 1, 'food_id': 1, 'number': 1});
db.detail.insertOne({'order_id': 1, 'food_id': 2, 'number': 2});
db.detail.insertOne({'order_id': 2, 'food_id': 1, 'number': 2});
db.detail.insertOne({'order_id': 3, 'food_id': 1, 'number': 1});