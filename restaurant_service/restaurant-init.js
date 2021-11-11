db.auth('comp3122', '23456')
db = db.getSiblingDB('Menu')

db.createCollection('menu');

db.menu.insertOne({'restaurant_id':1,'Food_id':1,'Food_Name':'Fishball', 'Food_Price': 5});
db.menu.insertOne({'restaurant_id':1,'Food_id':2,'Food_Name':'Siu mai', 'Food_Price': 7});
db.menu.insertOne({'restaurant_id':1,'Food_id':3,'Food_Name':'Rice flour roll', 'Food_Price': 12});

db.menu.insertOne({'restaurant_id':2,'Food_id':1,'Food_Name':'Chicken', 'Food_Price': 40});
db.menu.insertOne({'restaurant_id':2,'Food_id':2,'Food_Name':'Pork', 'Food_Price': 45});
db.menu.insertOne({'restaurant_id':2,'Food_id':3,'Food_Name':'Beaf', 'Food_Price': 50});

db.menu.insertOne({'restaurant_id':3,'Food_id':1,'Food_Name':'Curry rice', 'Food_Price': 35});
db.menu.insertOne({'restaurant_id':3,'Food_id':2,'Food_Name':'Hamburger', 'Food_Price': 30});
db.menu.insertOne({'restaurant_id':3,'Food_id':3,'Food_Name':'Ramen', 'Food_Price': 40});

