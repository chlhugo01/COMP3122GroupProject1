db.auth('comp3122', '23456')
db = db.getSiblingDB('order')

db.createCollection('receipts');
db.receipts.insertOne({'id': 1, 'customer_id': 4,'restaurant_id': 1, 'status': 'ordered'});
db.receipts.insertOne({'id': 2, 'customer_id': 3,'restaurant_id': 1, 'status': 'ordered'});
db.receipts.insertOne({'id': 3, 'customer_id': 2,'restaurant_id': 1, 'status': 'finished'});
db.receipts.insertOne({'id': 4, 'customer_id': 1,'restaurant_id': 2, 'status': 'finished'});

db.createCollection('details');
db.details.insertOne({'id': 1, 'receipt_id': 1, 'food_id': 1, 'number': 1});
db.details.insertOne({'id': 2, 'receipt_id': 1, 'food_id': 2, 'number': 1});
db.details.insertOne({'id': 3, 'receipt_id': 2, 'food_id': 1, 'number': 1});
db.details.insertOne({'id': 4, 'receipt_id': 3, 'food_id': 1, 'number': 1});
db.details.insertOne({'id': 4, 'receipt_id': 4, 'food_id': 1, 'number': 1});