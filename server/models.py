from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Initialize Flask-SQLAlchemy
db = SQLAlchemy()

# Define the Sighting model
class Sighting(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    time = db.Column(db.String)
    location = db.Column(db.String)
    shape_of_craft = db.Column(db.String)
    approximate_size = db.Column(db.Integer)
    approximate_speed = db.Column(db.Integer)
    description = db.Column(db.String)
    reporter = db.Column(db.String)
    reporter_reliable_witness = db.Column(db.Boolean)
    
    def __repr__(self):
        return f"<Sighting {self.id}>"