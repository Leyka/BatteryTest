from server import db
from datetime import datetime


class Battery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer, unique=True, nullable=False)
    model = db.Column(db.String)
    color = db.Column(db.String)
    used_by = db.Column(db.String)


class BatteryTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    battery_id = db.Column(db.Integer, db.ForeignKey('battery.id'), nullable=False)
    capacity_mah = db.Column(db.Integer, nullable=False)
    resistance_mohm = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.now())
