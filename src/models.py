from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship("Favorites", backref="User")
    

    def __repr__(self):
        return self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,            
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    alive = db.Column(db.Boolean(), unique=False, nullable=False, default=True)
    episode = db.relationship("Episodes", secondary="character_has_episodes", backref="Characters")
    location = db.relationship("Locations", secondary="character_has_locations", backref="Characters")
    favorites = db.relationship("Favorites", backref="Characters")
    
    def __repr__(self):
        return self.name
   
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender" : self.gender,
            "alive" : self.alive
            
        }
class Episodes(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    lenght = db.Column(db.Integer)    
    location = db.relationship("Locations", secondary="episode_has_locations", backref="Episodes")
    favorites = db.relationship("Favorites", backref="Episodes")

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lenght" : self.lenght,           
            
        }

class Locations(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    type = db.Column(db.String(250))           
    favorites = db.relationship("Favorites", backref="Locations")

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type" : self.type,           
            
        }


character_has_episodes= db.Table("character_has_episodes",
    db.Column("character_id", db.Integer, db.ForeignKey('characters.id'),nullable=False , primary_key=True),
    db.Column("episode_id", db.Integer, db.ForeignKey('episodes.id'),nullable=False , primary_key=True)
)

character_has_locations= db.Table("character_has_locations",
    db.Column("character_id", db.Integer, db.ForeignKey('characters.id'),nullable=False , primary_key=True),
    db.Column("location_id", db.Integer, db.ForeignKey('locations.id'),nullable=False , primary_key=True)
)
      
    
episode_has_locations= db.Table("episode_has_locations",
    db.Column("episode_id", db.Integer, db.ForeignKey('episodes.id'),nullable=False , primary_key=True),
    db.Column("location_id", db.Integer, db.ForeignKey('locations.id'),nullable=False , primary_key=True)
)
    

class Favorites(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    id_character = db.Column(db.Integer,db.ForeignKey('characters.id'))
    id_episode = db.Column(db.Integer, db.ForeignKey('episodes.id'))
    id_location = db.Column(db.Integer, db.ForeignKey('locations.id'))   

    def serialize(self):
        return {
            "id_user": self.id_user,
            "id_character": self.id_character,
            "id_episode" : self.id_episode,           
            "id_location" : self.id_location,
        }