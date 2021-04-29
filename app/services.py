from app.models import Battery, BatterySpec, BatteryTest
from app import db


class BatteryService:
    def get_or_create_battery(self, public_id) -> Battery:
        # Get battery by public id
        battery = Battery.query.filter_by(public_id=public_id).first()
        if battery is None:
            # Create
            battery = Battery(public_id)
            db.session.add(battery)
            db.session.commit()

        return battery


class BatterySpecService:
    def get_all_specs(self):
        return BatterySpec.query.all()

    def create_spec(self, manufacturer, model):
        spec = BatterySpec(manufacturer, model)
        db.session.add(spec)
        db.session.commit()


class BatteryTestService:
    def create_test(self, battery_id, capacity, resistance):
        test = BatteryTest(battery_id, capacity, resistance)
        db.session.add(test)
        db.session.commit()
