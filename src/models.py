import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    UserID = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    Address = Column(String(250),nullable=False)
    Password = Column(String(250),nullable=False)

class PeopleFavorites(Base):
    __tablename__ = 'PeopleFavorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    UserID = Column(Integer, ForeignKey('User.UserID'), primary_key=True)
    PeoplefavoritesID = Column(Integer, ForeignKey('People.PeopleID'),primary_key=True)
    
class PlanetFavorites(Base):
    __tablename__ = 'PlanetFavorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    UserID = Column(Integer, ForeignKey('User.UserID'), primary_key=True)
    PeoplefavoritesID = Column(Integer, ForeignKey('Planet.planetID'),primary_key=True)

class Planet(Base):
    __tablename__ = 'Planet'

    planetID = Column(Integer, primary_key=True )
    name = Column(String(250))
    diameter = Column(Integer)
    mass = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
   


   
     
class People(Base):
    __tablename__ = 'People'

    PeopleID = Column(Integer, primary_key=True )
    name = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color =  Column(String(250))
    gender = Column(String(250))
    


    def to_dict(self):
        return {}
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')