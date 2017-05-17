""" 
    models.plant
    ------

    Database model of the data obtained from the sensors of a plant.
"""

from extensions import db

class Plant(db.Model):
    __tablename__ = 'plant'

    id = db.Column(db.Integer, nullable=False, primary_key = True)
    name = db.Column(db.String(64), unique=True, index=True)
    temperature = db.Column(db.Float(), nullable=True)
    humidity = db.Column(db.Float(), nullable=True)
    moisture = db.Column(db.Integer(), nullable=True)
    illuminance = db.Column(db.Integer(), nullable=True)
    timestamp = db.Column(db.DateTime)
