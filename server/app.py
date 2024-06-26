#!/usr/bin/env python3

from models import db, Sighting
from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate

# import model and db instance

# Initialize Flask app
app = Flask(__name__)

# configure the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-Migrate
migrate = Migrate(app, db)
# Initialize the db instance
db.init_app(app)
# Define routes and views
@app.route("/")
def home():
    message = {"message": "The UAPID welcome our new extraterrestrial overlords!"}
    return make_response(jsonify(message), 200)

@app.route('/sightings')
def sightings():
    sightings=[]
    for sighting in Sighting.query.all():
        sightings.append(sighting.to_dict())
    body = {'sightings': sightings}
    return make_response(body, 200)

@app.route('/sightings/<int:id>')
def sighting_by_id(id):
    sightings_id = Sighting.query.filter(Sighting.id == id).first()
    body = {'sighting ids': sightings_id.to_dict()}
    return make_response(body, 200)

@app.route('/sightings/location/<string:location>')
def locations(location):
    sightings_location = Sighting.query.filter(Sighting.location == location).first()
    body = {'sighting locations': sightings_location.to_dict()}
    return make_response(body, 200)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
