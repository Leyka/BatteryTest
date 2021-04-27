from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from settings import DATABASE_URI

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# ==== HTML =====
@app.route('/')
def dashboard_view():
    return render_template('index.html')


@app.route('/battery/<int:battery_id>')
def battery_view(battery_id):
    return render_template('battery.html', battery_id=battery_id)


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
