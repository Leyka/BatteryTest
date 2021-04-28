from app import app
from flask import render_template, request


# ==== HTML =====
@app.route('/')
def dashboard():
    return render_template('index.html')


@app.route('/doc')
def doc():
    return render_template('doc.html')


@app.route('/battery/<int:battery_id>')
def battery(battery_id):
    return render_template('battery.html', battery_id=battery_id)


@app.route('/specs')
def specs():
    return render_template('specs/index.html')


@app.route('/specs/new', methods=['GET', 'POST'])
def specs_new():
    if request.method == 'GET':
        return render_template('specs/new.html')


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

    return payload