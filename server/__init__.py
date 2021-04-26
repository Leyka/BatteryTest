from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from settings import DATABASE_URI

app = Flask(__name__)

# Configure database
print(DATABASE_URI)
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
if __name__ == '__main__':
    app.run()
