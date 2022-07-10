import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self_username

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False, unique=True)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    url = Column(String(50), nullable=False, unique=True)

class Vehicles(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    vehicle_class = Column(String(50), nullable=False)
    manufacturer = Column(Integer, nullable=False)
    url = Column(String(50), nullable=False, unique=True)

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class Relational_favorite_user(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_user = Column(Integer, primary_key=True)
    name_user = Column(String(50), nullable=False)
    id_character = Column(Integer, nullable=False)
    name_character = Column(String(50), nullable=False)
    id_planet = Column(Integer, nullable=False)
    name_planet = Column(String(50), nullable=False)
    id_vehicle = Column(Integer, nullable=False)
    name_vehicle = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False, unique=True)


  

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')