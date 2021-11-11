db.auth('comp3122', '23456')
db = db.getSiblingDB('Menu')

db.createCollection('menu');

db.order.insertOne({'restaurant_id':1,'Food_id':1,'Food_Name':'Potato', 'Food_Price': 10});
db.order.insertOne({'restaurant_id':1,'Food_id':2,'Food_Name':'Tomato', 'Food_Price': 15});
db.order.insertOne({'restaurant_id':1,'Food_id':3,'Food_Name':'Fish', 'Food_Price': 20});

