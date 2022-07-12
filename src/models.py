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
    character_favorite = relationship("Character_Favorite", back_populates="person")
    vehicles_favorite = relationship("Vehicles_Favorite", back_populates="person")
    planets_favorite = relationship("Planets_Favorite", back_populates="person")

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))
    character_favorite_id = Column(Integer, ForeignKey("character_favorite.id"))
    character_favorite = relationship("Character_Favorite", back_populates="character")
    
    
    

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))

    vehicles_favorite_id = Column(Integer, ForeignKey("vehicles_favorite.id"))
    vechicles_favorite = relationship("Vehicles_Favorite", back_populates="vehicles")
  

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))

    planets_favorite_id = Column(Integer, ForeignKey("planets_favorite.id"))
    planets_favorite = relationship("Planet_Favorite", back_populates="planets")


class Character_Favorite(Base):
    __tablename__ = 'character_favorite'
    id = Column(Integer, primary_key=True)
    #relacion person y favorite
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    person_name = Column(String(50))
    #relacion characters y favorite
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    character_name = Column(String(50))

    person_id = Column(Integer, ForeignKey("person.id", back_populates="character_favorite"))

    character = relationship("Character")

class Vehicles_Favorite(Base):
    __tablename__ = 'vehicles_favorite'
    id = Column(Integer, primary_key=True)
    #relacion person y favorite
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    person_name = Column(String(50))
    #relacion vehicles y favorite
    vehicle_id = Column(Integer, ForeignKey('vechicles.id'))
    vehicle = relationship(Vehicles)
    vehicle_name = Column(String(50))

    person_id = Column(Integer, ForeignKey("person.id", back_populates="vehicles_favorite"))

    vehicles = relationship("Vehicles")



class Planets_Favorite(Base):
    __tablename__ = 'planets_favorite'
    id = Column(Integer, primary_key=True)
    #relacion person y favorite
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    person_name = Column(String(50))
    #relacion planets y favorite
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    planet_name = Column(String(50))

    person_id = Column(Integer, ForeignKey("person.id"))

    planets = relationship("Planets", back_populates="planets_favorite")

    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')