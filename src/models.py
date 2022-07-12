import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorites = relationship("Favorite", back_populates="person")

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))
    favorite_id = Column(Integer, ForeignKey("favorite.id"))
    favorite = relationship("Favorite", back_populates="character")
    

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))
    favorite_id = Column(Integer, ForeignKey("favorite.id"))
    favorite = relationship("Favorite", back_populates="vehicles")

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))
    favorite_id = Column(Integer, ForeignKey("favorite.id"))
    favorite = relationship("Favorite", back_populates="planets")

class Favorite(Base):
    __tablename__ = 'favorite'
    #relacion person y favorite
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    person_name = Column(String(50))
    #relacion characters y favorite
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    character_name = Column(String(50))
    #relacion vehicles y favorite
    vehicle_id = Column(Integer, ForeignKey('vechicles.id'))
    vehicle = relationship(Vehicles)
    vehicle_name = Column(String(50))
    #relacion planets y favorite
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    planet_name = Column(String(50))
    #relacion uno a muchos person y favorite, donde favorite sería hijo
    person_id = Column(Integer, ForeignKey("person.id"))
    person = relationship("Person", back_populates="favorite")
    #relacion uno a muchos character, planet, vehicle y favorite donde sería padre
    favorite_character = relationship("Character", back_populates="favorite")
    favorite_planet = relationship("Planets", back_populates="favorite")
    favorite_vehicle = relationship("Vehicles", back_populates="favorite")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')