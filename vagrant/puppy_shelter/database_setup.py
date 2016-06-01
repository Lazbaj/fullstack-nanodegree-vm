import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    address = Column(String(80))
    city = Column(String(20))
    state = Column(String(20))
    zipCode = Column(String(8))
    website = Column(String(80))

class Puppy(Base):
    __tablename__ = 'puppy'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    date_of_birth = Column(Date)
    gender = Column(String(8))
    weight = Column(String(8))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)


##### Insert at the end of file #####
engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)
