from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(20))
    zipCode = Column(String(10))
    website = Column(String)

class Puppy(Base):
    __tablename__ = 'puppy'

    name = Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)
    gender = Column(String(6), nullable = False)
    date_of_birth = Column(Date)
    picture = Column(String)
    weight = Column(Numeric(10))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)


##### Insert at the end of file #####
engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)
