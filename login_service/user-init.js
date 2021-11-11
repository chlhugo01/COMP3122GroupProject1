db.auth('comp3122', '23456')
db = db.getSiblingDB('user')

db.createCollection('customer');
db.costomer.insertOne({'customer_id':1, 'username':'Alice', 'password':'Alice123','Address':'Hong Kong Happy House', 'phone_number': 92410781});
db.costomer.insertOne({'customer_id':2, 'username':'May', 'password':'May123','Address':'Hong Kong Exciting House', 'phone_number': 94356213});
db.costomer.insertOne({'customer_id':3, 'username':'Anson','password':'Anson123', 'Address':'Hong Kong Playing House', 'phone_number': 97325641});

db.createCollection('restaurant');
db.restaurant.insertOne({'restaurant_id':1, 'username':'Bob', 'password':'Bob123','Address':'Hong Kong Happy Dim Sum', 'phone_number': 25309035});
db.restaurant.insertOne({'restaurant_id':2, 'username':'John', 'password':'John123','Address':'Hong Kong Happy Meal', 'phone_number': 24569632});
db.restaurant.insertOne({'restaurant_id':3, 'username':'William','password':'William123', 'Address':'Hong Kong Happy Restaurant', 'phone_number': 27543684});

db.createCollection('delivery');
db.delivery.insertOne({'delivery_id':1, 'username':'David','password':'David123', 'phone_number': 95326188});
db.delivery.insertOne({'delivery_id':2, 'username':'Thomas','password':'Thomas123', 'phone_number': 93457654});
db.delivery.insertOne({'delivery_id':3, 'username':'Harry','password':'Harry123', 'phone_number': 98657731});

db.createCollection('admin');
db.admin.insertOne({'admin_id':1, 'username':'Peter','password':'Peter123'});
