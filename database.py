"""
Run this script to create a fresh database
"""
from server import db
from sqlalchemy_utils import database_exists
from settings import DEBUG, DATABASE_URI

delete_db = True

if database_exists(DATABASE_URI) and not DEBUG:
    answer = input("Are you sure to delete the existing database and recreate a new one? (y/n): ")
    delete_db = answer.lower() == 'y' or answer.lower() == 'yes'

if delete_db:
    db.reflect()
    db.drop_all()
    db.create_all()
