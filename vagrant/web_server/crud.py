from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

### Functions used in webserver.py ###

## Return all the item in 'Restaurant' table
def getRestaurants():
    restaurants = session.query(Restaurant.name, Restaurant.id).order_by(Restaurant.name.asc()).all()
    return restaurants

## Create a new entry for the table 'Restaurant'
def addRestaurant(new_name):
    new_restaurant = Restaurant(name = new_name)
    session.add(new_restaurant)
    session.commit()

## Delete a specific entry in the table 'Restaurant'
def deleteRestaurant(restaurant_id):
    to_delete = session.query(Restaurant).filter_by(id = restaurant_id).one()
    session.delete(to_delete)
    session.commit()


### Other examples from first lesson ###

## Create a new entry for the table 'Restaurant'
# myFirstRestaurant = Restaurant(name = 'Pizza Palace')
# session.add(myFirstRestaurant)
# session.commit()

## Query for all elements in the table 'Restaurant'
#print session.query(Restaurant).all()

## Create a new entry for the table "MenuItem"
# cheesepizza = MenuItem(name = 'Cheese Pizza',
#                        description = 'Made with all natural ingredients!',
#                        course = 'Entree', price = '$8.99',
#                        restaurant = myFirstRestaurant)
# session.add(cheesepizza)
# session.commit()

## Query for all elements in the table 'MenuItem'
#print session.query(MenuItem).all()

## Query for the first element in table 'Restaurant' and print its name
# firsResult = session.query(Restaurant).first()
# print firsResult.name

## Print names of all elements in table 'Restaurant'
# restaurants = session.query(Restaurant).all()
# for restaurant in restaurants:
#     print restaurant.name
#     print restaurant.id

## Print names of all elements in table 'MenuItem'
# items = session.query(MenuItem).all()
# for item in items:
#     print item.name
#     print item.restaurant_id

## Return the number of elements in table 'Restaurant' and 'MenuItem'
# print session.query(Restaurant).count()
# print session.query(MenuItem).count()

## Select all the "Veggie Burger" from 'MenuItem' and print their parameters
# veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
# for veggieBurger in veggieBurgers:
#     print veggieBurger.id
#     print veggieBurger.price
#     print veggieBurger.restaurant.name
#     print '\n'

## Select a single element (one()) from 'MenuItem' with id=8 and update price
# UrbanVeggieBurgers = session.query(MenuItem).filter_by(id = 10).one()
# UrbanVeggieBurgers.price = '$2.99'
# session.add(UrbanVeggieBurgers)
# session.commit()

## Update the price of all 'Veggie Burger' in 'MenuItem'
# for veggieBurger in veggieBurgers:
#     if veggieBurger.price != '$2.99':
#         veggieBurger.price = '$2.99'
#         session.add(veggieBurger)
#         session.commit()

## Select an item and delete it
# spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
# session.delete(spinach)
# session.commit()
