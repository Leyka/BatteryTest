"""
Run this script to create a fresh database
"""
from server import db
from server import models
from sqlalchemy_utils import database_exists
from settings import DEBUG, DATABASE_URI

delete_db = True

if database_exists(DATABASE_URI) and not DEBUG:
    answer = input("Are you sure to delete the existing database and recreate a new one? (y/n): ")
    delete_db = answer.lower() == 'y'

if delete_db:
    db.reflect()
    db.drop_all()
    db.create_all()
    print(f"Database successfully created at: {DATABASE_URI}")
