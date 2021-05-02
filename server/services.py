from statistics import mean
from server.models import Battery, BatterySpec, BatteryTest
from server.viewmodels import BatteryTestStats
from server import db


class BatteryService:
    def get_all_batteries(self):
        return Battery.query.all()

    def get_battery_by_public_id(self, public_id):
        return Battery.query.filter_by(public_id=public_id).first()

    def get_or_create_battery(self, public_id) -> Battery:
        # Get battery by public id
        battery = self.get_battery_by_public_id(public_id)
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

    def get_stats(self, battery):
        stats = BatteryTestStats()
        # Capacity
        capacities = list(map(lambda t: t.capacity_mah, battery.tests))
        stats.avg_capacity = round(mean(capacities))
        stats.min_capacity = min(capacities)
        stats.max_capacity = max(capacities)
        # Resistance
        resistances = list(map(lambda t: t.resistance_mohm, battery.tests))
        stats.avg_resistance = mean(resistances)
        stats.min_resistance = min(resistances)
        stats.max_resistance = max(resistances)

        return stats
