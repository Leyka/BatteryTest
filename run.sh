#!/bin/sh

# Set default db path if not set
if [ -z "$DB_PATH" ]; then
  DB_PATH="./db/battery.db"
fi

# Check if DB file exists
if [ ! -f "$DB_PATH" ]; then
  python3 manage.py createdb
fi

gunicorn server:app --workers 4 -b 0.0.0.0:80
