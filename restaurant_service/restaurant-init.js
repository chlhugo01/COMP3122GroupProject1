db.auth('comp3122', '23456')
db = db.getSiblingDB('Restaurant')

db.createCollection('restaurants');
db.restaurants.insertOne({'id': 1, 'name': 'hk happy meal 1', 'address': 'Hong Kong A', 'phone_number': 12345678});
db.restaurants.insertOne({'id': 2, 'name': 'hk happy meal 2', 'address': 'Hong Kong B', 'phone_number': 23231478});
db.restaurants.insertOne({'id': 3, 'name': 'hk happy meal 3', 'address': 'Hong Kong C', 'phone_number': 54326728});

db.createCollection('menu');
db.menu.insertOne({'id': 1, 'restaurant_id':1, 'name': 'Fishball', 'price': 5});
db.menu.insertOne({'id': 2, 'restaurant_id':1, 'name': 'Siu mai', 'price': 7});
db.menu.insertOne({'id': 3, 'restaurant_id':1, 'name': 'Rice flour roll', 'price': 12});
db.menu.insertOne({'id': 4, 'restaurant_id':2, 'name': 'Chicken', 'price': 40});
db.menu.insertOne({'id': 5, 'restaurant_id':2, 'name': 'Pork', 'price': 45});
db.menu.insertOne({'id': 6, 'restaurant_id':2, 'name': 'Beaf', 'price': 50});
db.menu.insertOne({'id': 7, 'restaurant_id':3, 'name': 'Curry rice', 'price': 35});
db.menu.insertOne({'id': 8, 'restaurant_id':3, 'name': 'Hamburger', 'price': 30});
db.menu.insertOne({'id': 9, 'restaurant_id':3, 'name': 'Ramen', 'price': 40});