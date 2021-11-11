# COMP3122 - Service details
## Service 0 - login:
|docker               |name                     |ports|
|---------------------|---------------          |-----|
| db image :          | mongo_user              |     |
| service image :     | login_service           |     |
| db container :      | db0                     |27100|
| service container : | c0                      |15100|
## Service 1 - restaurant:
|docker               |name                     |ports|
|---------------------|---------------          |-----|
| db image :          | mongo_restaurant        |     |
| service image :     | restaurant_service      |     |
| db container :      | db1                     |27101|
| service container : | c1                      |15101|

## Service 2 - order
|docker               |name                     |ports|
|---------------------|-----------------        |-----|
| db image :          | mongo_order             |     |
| service image :     | order_service           |     |
| db container :      | db2                     |27102|
| service container : | c2                      |15102|

## Not updated


## Service 3 - Update: **tbc**
|docker               |name                     |ports|
|---------------------|------------------       |-----|
| db image :          | mongo_update            |     |
| service image :     | update_service          |     |
| db container :      | db3                     |27103|
| service container : | s3                      |15103|

## Service 4 - Receive Order (restaurant):
|docker               |name                     |ports|
|---------------------|-------------------      |-----|
| db image:           | mongo_restaurant        |     |
| service image :     | restaurant_service      |     |
| db container :      | db4                     |27104|
| service container : | s4                      |15104|

## Service 5 - Receive Order (delivery):
|docker               |name                     |ports|
|---------------------|------------------       |-----|
| db image :          | mongo_delivery          |     |
| service image :     | delivery_service        |     |
| db container :      | db5                     |27105|
| service container : | s5                      |15105|

## Service 6 - Instant Messaging: **tbc**
|docker               |name                     |ports|
|---------------------|------------------       |-----|
| db image :          | mongo_message           |     |
| service image :     | message_service         |     |
| db container :      | db6                     |27106|
| service container : | s6                      |15106|

## Service 7 - Location of Delivery Man: **tbc**
|docker               |name                     |ports|
|---------------------|------------------       |-----|
| db image :          | mongo_location          |     |
| service image :     | location_service        |     |
| db container :      | db7                     |27107|
| service container : | s7                      |15107|

## Service 8 - Rating: **tbc**
|docker               |name                     |ports|
|---------------------|------------------       |-----|
| db image :          | mongo_rating            |     |
| service image :     | rating_service          |     |
| db container :      | db8                     |27108|
| service container : | s8                      |15108|

# Useful Command
