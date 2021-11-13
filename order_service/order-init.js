db.auth('comp3122', '23456')
db = db.getSiblingDB('order')

db.createCollection('receipts');
db.receipts.insertOne({'id': 1, 'customer_id': 0,'restaurant_id': 1});
db.receipts.insertOne({'id': 2, 'customer_id': 0,'restaurant_id': 1});
db.receipts.insertOne({'id': 3, 'customer_id': 0,'restaurant_id': 3});
db.receipts.insertOne({'id': 4, 'customer_id': 0,'restaurant_id': 2});

db.createCollection('details');
db.details.insertOne({'id': 1, 'receipts_id': 1, 'food_id': 1, 'number': 1, 'price': 5});