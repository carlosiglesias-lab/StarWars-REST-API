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
from models import db, Users, Characters, Episodes, Locations,Favorites
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

@app.route('/users', methods=['GET'])
def get_all_users():
    users = Users.query.all()
    user_serialized = [x.serialize() for x in users]
    return jsonify({"Usuarios:" : user_serialized}), 200 

@app.route('/users/favorites', methods=['GET'])
def get_all_users():    
    user_id = request.json.get("user_id") 
    favorites = Favorites.query.filter_by(id_user = user_id)
    favorites_serialized = [x.serialize() for x in favorites]
    return jsonify({"Favoritos de Usuario:" : favorites_serialized}), 200 

@api.route('/favorites/characters/<id>', methods=['POST'])
def new_character_fav(id):
    user_id = request.json.get("user_id")    
    db.session.add(Favorites (user_id=user_id, id_character=id))
    db.session.commit()
    return jsonify({"response": "Character added to favorites succesfully"}), 200

@api.route('/favorites/characters/<id>', methods=['DELETE'])
def delete_character_favorite(id):
    user_id = request.json.get("user_id") 
    favorite =  Favorites.query.filter_by(id_user=user_id,id_character=id).first()
    db.session.delete(favorite)    
    db.session.commit()
    return jsonify({"response": "Favorite deleted successfully"}), 200  

@api.route('/favorites/locations/<id>', methods=['POST'])
def new_character_fav(id):
    user_id = request.json.get("user_id")    
    db.session.add(Favorites (user_id=user_id, id_location=id))
    db.session.commit()
    return jsonify({"response": "Location added to favorites succesfully"}), 200

@api.route('/favorites/location/<id>', methods=['DELETE'])
def delete_location_favorite(id):
    user_id = request.json.get("user_id") 
    favorite =  Favorites.query.filter_by(id_user=user_id,id_location=id).first()
    db.session.delete(favorite)    
    db.session.commit()
    return jsonify({"response": "Favorite deleted successfully"}), 200

@app.route('/characters', methods=['GET'])
def all_characters():
    characters = Characters.query.all()
    character_serialized = [x.serialize() for x in characters]
    return jsonify({"Characters:" : character_serialized}), 200

@app.route('/characters/<id>', methods=['GET'])
def single_charactere(id):    
    character = Characters.query.get(id)    
    return jsonify({"Character:" : character.serialize()}), 200

@app.route('/episodes', methods=['GET'])
def all_episodes():
    episodes = Episodes.query.all()
    episodes_serialized = [x.serialize() for x in episodes]
    return jsonify({"Episodios:" : episodes_serialized}), 200

@app.route('/episodes/<id>', methods=['GET'])
def single_episode(id):    
    episode = Episodes.query.get(id)    
    return jsonify({"Character:" : episode.serialize()}), 200

@app.route('/locations', methods=['GET'])
def all_locations():
    locations = Locations.query.all()
    location_serialized = [x.serialize() for x in locations]
    return jsonify({"Locations:" : location_serialized}), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
