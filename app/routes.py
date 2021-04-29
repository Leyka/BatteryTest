from app import app
from flask import render_template, request, redirect, url_for
from app.services import BatteryService, BatterySpecService, BatteryTestService

battery_service = BatteryService()
spec_service = BatterySpecService()
test_service = BatteryTestService()

# ==== HTML =====


@app.route('/')
def dashboard():
    batteries = battery_service.get_all_batteries()
    return render_template('index.html', batteries=batteries)


@app.route('/doc')
def doc():
    return render_template('doc.html')


@app.route('/battery/<int:battery_id>')
def battery(battery_id):
    return render_template('battery.html', battery_id=battery_id)


@app.route('/specs')
def specs():
    all_specs = spec_service.get_all_specs()
    return render_template('specs/index.html', specs=all_specs)


@app.route('/specs/new', methods=['GET', 'POST'])
def specs_new():
    if request.method == 'GET':
        return render_template('specs/new.html')
    elif request.method == 'POST':
        manufacturer = request.form['manufacturer']
        model = request.form['model']
        spec_service.create_spec(manufacturer, model)
        return redirect(url_for('specs'))


# ==== API =====
@app.route('/api/tests', methods=['POST'])
def api_battery_test():
    """
    Example payload to keep it simple for arduino:
    {
        "public_id": 1,
        "capacity_mah": 2000,
        "resistance_mohm": 10
    }
    """
    payload = request.json
    if payload is None:
        return "You must provide a JSON payload.", 400

    public_id = payload["public_id"]
    capacity = payload["capacity_mah"]
    resistance = payload["resistance_mohm"]

    # Get or create battery
    battery = battery_service.get_or_create_battery(public_id)
    test = test_service.create_test(battery.id, capacity, resistance)
    return 'OK'
