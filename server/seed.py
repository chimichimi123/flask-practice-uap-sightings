# import app
from app import app
# import model and db instance
from models import db, Sighting
# Define seeding functions (optional: use Faker to help generate fake data)
def seed_sightings():
    sightings = [
        Sighting(date="2021-01-01", time="12:00", location="New York City", shape_of_craft="Triangle", approximate_size=100, approximate_speed=100, description="A large triangle-shaped craft was seen flying over the city.", reporter="John Doe", reporter_reliable_witness=True),
        Sighting(date="2021-01-02", time="13:00", location="Los Angeles", shape_of_craft="Circle", approximate_size=50, approximate_speed=50, description="A small circle-shaped craft was seen flying over the city.", reporter="Jane Doe", reporter_reliable_witness=False),
        Sighting(date="2021-01-03", time="14:00", location="Chicago", shape_of_craft="Square", approximate_size=75, approximate_speed=75, description="A medium square-shaped craft was seen flying over the city.", reporter="John Smith", reporter_reliable_witness=True),
    ]
    db.session.bulk_save_objects (sightings)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        seed_sightings()
        pass
