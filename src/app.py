"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))
    return jsonify(all_users), 200

@app.route('/user', methods=['POST'])
def create_new_users():
    request_body = request.get_json()
    user = User(email = request_body["email"], password = request_body["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user,"user successfully created"), 200

@app.route('/character', methods=['GET'])
def get_all_chacters():
    character = Character.query.all()
    all_characters = list(map(lambda x: x.serialize(), character))
    return jsonify(all_characters), 200

@app.route('/character/<int:id>', methods=["GET"])
def get_each_character(id):
    character = Character.query.get(id)
    return jsonify(character.serialize()),200

@app.route('/character/<int:id>', methods=["DELETE"])
def delete_character(id):
    character = Character.query.get(id)
    db.session.delete(character)
    db.session.commit()
    return jsonify("character deleted"), 200

@app.route('/character', methods=['POST'])
def create_new_character():
    request_body = request.get_json()
    character = Character(height = request_body["height"], firstname = request_body["firstname"], lastname = request_body["lastname"])
    db.session.add(character)
    db.session.commit()
    return jsonify(character.serialize(),"character successfully created"), 200

@app.route('/planets', methods=['GET'])
def get_all_planets():
    planets = Planet.query.all()
    all_planets = list(map(lambda x: x.serialize(), planets))
    return jsonify(all_planets), 200

@app.route('/planets/<int:id>', methods=["GET"])
def get_each_planet(id):
    planet = Planet.query.get(id)
    return jsonify(planet.serialize()),200

@app.route('/planets/<int:id>', methods=["DELETE"])
def delete_planet(id):
    planet = Planet.query.get(id)
    db.session.delete(planet)
    db.session.commit()
    return jsonify("planet deleted"), 200

@app.route('/planets', methods=['POST'])
def create_new_planet():
    request_body = request.get_json()
    planet = Planet(climate = request_body["climate"], terrain = request_body["terrain"])
    db.session.add(planet)
    db.session.commit()
    return jsonify(planet.serialize(),"planet successfully created"), 200

@app.route('/favorites', methods=['GET'])
def get_all_favorites():
    favorites = Favorites.query.all()
    all_favorites = list(map(lambda x: x.serialize(), favorites))
    return jsonify(all_favorites), 200

@app.route('/favorites/<int:id>', methods=["GET"])
def get_each_favorite(id):
    favorites = Favorites.query.get(id)
    return jsonify(favorites.serialize()),200

@app.route('/favorites/<int:id>', methods=["DELETE"])
def delete_favorites(id):
    favorites = Favorites.query.get(id)
    db.session.delete(favorites)
    db.session.commit()
    return jsonify("favorite deleted"), 200

@app.route('/favorites', methods=['POST'])
def create_new_favorite():
    request_body = request.get_json()
    favorites = Favorites(user = request_body["user"], character = request_body["character"],planet = request_body["planet"])
    db.session.add(favorites)
    db.session.commit()
    return jsonify(favorites,"planet successfully created"), 200

    
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
