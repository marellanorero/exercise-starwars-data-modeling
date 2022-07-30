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
    character_favorite = relationship("Character_Favorite", secondary="character_favorite")
    planets_favorite = relationship("Planets_Favorite", secondary="planets_favorite")

    
class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))
    person = relationship("Person", secondary="character_favorite")
      
class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))
    person = relationship("Person", secondary="planets_favorite")

class Character_Favorite(Base):
    __tablename__ = 'character_favorite'
    #relacion person y favorite -- Muchos a muchos ... muchos usuarios pueden tener muchos favoritos
    person_id= Column(Integer, ForeignKey('person.id'), primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'), primary_key=True)

class Planets_Favorite(Base):
    __tablename__ = 'planets_favorite'
    #relacion person y favorite -- Muchos a muchos ... muchos usuarios pueden tener muchos favoritos
    person_id= Column(Integer, ForeignKey('person.id'), primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)

    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')