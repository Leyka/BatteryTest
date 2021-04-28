"""
BatterySpec 1 -- *   Battery
Battery     1 -- *   BatteryTest
"""

from app import db
from datetime import datetime


class Battery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer, unique=True, nullable=False)
    color = db.Column(db.String)
    used_by = db.Column(db.String)
    spec_id = db.Column(db.Integer, db.ForeignKey('battery_spec.id'))


class BatterySpec(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String)
    model = db.Column(db.String)


class BatteryTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    battery_id = db.Column(db.Integer, db.ForeignKey('battery.id'), nullable=False)
    capacity_mah = db.Column(db.Integer, nullable=False)
    resistance_mohm = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.now())
