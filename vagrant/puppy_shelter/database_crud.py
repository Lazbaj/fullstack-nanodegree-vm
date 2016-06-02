from datetime import date

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppyshelter.db')
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



## Query1 : Query all of the puppies and return the results in ascending alphabetical order

# puppies = session.query(Puppy).order_by(Puppy.name.asc()).all()
# for pup in puppies:
#     print pup.name


## Query2: Query all of the puppies that are less than 6 months old organized by the youngest first
# today_date = date.today()

# puppies = session.query(Puppy).order_by(Puppy.date_of_birth.desc()).all()
# for pup in puppies:
#     if (today_date - pup.date_of_birth).days < 6*30:
#         print 'Name: ' + pup.name + ' - Date of birth: ' + str(pup.date_of_birth)


## Query3: Query all puppies by ascending weight
# puppies = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight.asc()).all()
# for pup in puppies:
#     print 'Name: ' + pup.name + ' - Weight: ' + str(pup.weight)


## Query4: Query all puppies grouped by the shelter in which they are staying
# result = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()
# for item in result:
#     print 'Name: ' + item[0].name + ' - Shelter_ID: ' + str(item[0].id) + ' - Puppies: ' + str(item[1])

result = session.query(Puppy).order_by(Puppy.shelter_id).all()
for item in result:
    print 'Name: ' + item.name + ' - Shelter_ID: ' + str(item.shelter_id) + ' - Shelter Name: ' + item.shelter.name
