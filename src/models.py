import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

people_user = Table(
    'people_user',
    Base.metadata,
    Column('people_id', ForeignKey('people.id')),
    Column('users_id', ForeignKey('users.id'))
)
 
planets_user = Table(
    'planets_user',
    Base.metadata,
    Column('planets_id', ForeignKey('planets.id'), primary_key=True),
    Column('users_id', ForeignKey('users.id'), primary_key=True)
)

vehicles_user = Table(
    'vehicles_user',
    Base.metadata,
    Column('vehicles_id', ForeignKey('vehicles.id'), primary_key=True),
    Column('users_id', ForeignKey('users.id'), primary_key=True)
)



class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    unsername = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    people_user = relationship('Person', secondary="people_user", backref='users') # JOIN SQL MANY TO MANY
    planets_user = relationship('Planet', secondary="planets_user", backref='users') # JOIN SQL MANY TO MANY
    vehicles_user = relationship('Vehicle', secondary="vehicles_user", backref='users') # JOIN SQL MANY TO MANY

class Vehicle(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    #users = db.relationship("User", secondary="character_favorite")


class Person(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    #users = db.relationship("User", secondary="character_favorite")
    #users = db.relationship('User', cascade="all, delete", secondary="characters_favorites")


class Planet(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    #users = db.relationship("User", secondary="character_favorite")




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')