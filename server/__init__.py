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
        "battery": {
            "public_id": 1
            ...
        },
        "test": {
            "capacity_mah": 1200
            ...
        }
    }
    """
    payload = request.json
    # Test payload
    if payload is None:
        return "You must provide a JSON payload.", 400
    if not ('battery' in payload or 'test' in payload):
        return "Your payload must contain 'battery' and 'test' key.", 400

    return payload


if __name__ == '__main__':
    app.run()
