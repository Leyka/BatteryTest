from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URI, DEBUG

app = Flask(__name__)

app.config['DEBUG'] = DEBUG

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Once everything is configured, we can import routes
from app import routes
