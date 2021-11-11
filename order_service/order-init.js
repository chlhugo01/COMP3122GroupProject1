db.auth('comp3122', '23456')
db = db.getSiblingDB('order')

db.createCollection('record');
db.admin.insertOne({'record_id':1, 'costomer_id':1, 'restaurant_id':1, 'delivery_id':1});