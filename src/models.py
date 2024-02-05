from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
db = SQLAlchemy()

class User (db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    email = db.column(db.String(250))
    password = db.column(db.String(50))
    favorites = db.relationship("Favorites", back_populates="user")

class Character (db.Model):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.String(250))
    firstname = db.Column(db.String(250))
    lastname = db.Column(db.String(250), nullable=False)
   
class Planet (db.Model):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))

class Favorites (db.Model):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    list_of_favorites = db.Column(db.String(250))
    user = db.relationship("User", back_populates="favorites")
    character = db.relationship("Character")
    planet = db.relationship("Planet")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))