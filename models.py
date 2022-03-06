from flask_login import UserMixin
from __init__ import db
from datetime import datetime, date


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000)) #First name + Last name
    phone = db.Column(db.String(100))
    driving_license_number = db.Column(db.String(1000))
    D_O_B = db.Column(db.String(1000))
    license_plate_number = db.Column(db.String(1000))
    card_number = db.Column(db.String(1000))
    card_expiry = db.Column(db.String(1000))
    cvv = db.Column(db.Integer())


class Reserve(UserMixin, db.Model):
    name = db.Column(db.String(1000), primary_key=True) #First name + Last name
    parking_spot_number=db.Column(db.Integer())
    Parking_start_datetime= db.Column(db.String(1000))
    Parking_end_datetime= db.Column(db.String(1000))
    
