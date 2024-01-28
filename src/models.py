from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
db = SQLAlchemy()

class User (db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    email = db.column(db.string(250), nullable = False)
    password = db.column(db.string(50), nullable = False)
    favorites = db.relationship("Favorites", back_populates="user")

class Character (db.Model):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.String(250))
    firstname = db.Column(db.String(250))
    lastname = db.Column(db.String(250), nullable=False)
   
class Spaceship (db.Model):
    __tablename__ = 'spaceship'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(250))
    model = db.Column(db.String(250))

class Favorites (db.Model):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    list_of_favorites = db.Column(db.String(250))
    user = db.relationship("User", back_populates="favorites")
    character = db.relationship("Character")
    starship = db.relationship("Spaceship")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    starship_id = db.Column(db.Integer, db.ForeignKey('spaceship.id'))