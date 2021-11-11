db.auth('comp3122', '23456')
db = db.getSiblingDB('user')

db.createCollection('costomer');
db.costomer.insertOne({'costomer_id':1, 'username':'Alice', 'Address':'Hong Kong Happy House', 'phone_number': 92410781});

db.createCollection('restaurant');
db.restaurant.insertOne({'restaurant_id':1, 'username':'Bob', 'Address':'Hong Kong Happy Meal', 'phone_number': 25309035});

db.createCollection('delivery');
db.delivery.insertOne({'delivery_id':1, 'username':'David', 'phone_number': 95326188});

db.createCollection('admin');
db.admin.insertOne({'admin_id':1, 'username':'Peter'});