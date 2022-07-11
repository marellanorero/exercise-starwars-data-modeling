import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

association_association_character_favorite = Table(
    "association_character_favorite",
    Base.metadata,
    Column("character_id", ForeignKey("character.id"), primary_key=True),
    Column("favorite_id", ForeignKey("favorite.id"), primary_key=True),
)
association_association_planets_favorites = Table(
    "association_planets_favorites",
    Base.metadata,
    Column("planets_id", ForeignKey("planets.id"), primary_key=True),
    Column("favorite_id", ForeignKey("favorite.id"), primary_key=True),
)

association_association_vehicles_favorites = Table(
    "association_vehicles_favorites",
    Base.metadata,
    Column("vehicles_id", ForeignKey("vehicles.id"), primary_key=True),
    Column("favorite_id", ForeignKey("favorite.id"), primary_key=True),
)

association_association_favorites_users = Table(
    "association_favorites_users",
    Base.metadata,
    Column("users_favorites_id", ForeignKey("users_favorites.id"), primary_key=True),
    Column("favorite_id", ForeignKey("favorite.id"), primary_key=True),
)

association_association_users_favorites = Table(
    "association_users_favorites",
    Base.metadata,
    Column("users_favorites_id", ForeignKey("users_favorites.id"), primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True),
)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())
    favorites = relationship("Favorite", back_populates="user")

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
    favorite = relationship(
        "favorite", secondary=association_table, back_populates="characters"
    )

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
    favorite = relationship(
        "Favorite", secondary=association_table, back_populates="planets"
    )

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    vehicle_class = Column(String(50), nullable=False)
    manufacturer = Column(Integer, nullable=False)
    url = Column(String(50), nullable=False, unique=True)
    favorite = relationship(
        "Favorite", secondary=association_table, back_populates="vehicles"
    )

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    category = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="favorite")
    relacion = relationship(
        "Relational_favorite_user", secondary=association_table, back_populates="favorites"
    )

class Relational_favorite_user(Base):
    __tablename__ = 'users_favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'))
    category = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    favorite = relationship(
        "favorite", secondary=association_table, back_populates="relational_favorite_user"
    )

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')