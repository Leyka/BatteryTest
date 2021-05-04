import os
from os.path import join, dirname
from dotenv import load_dotenv

current_dir = dirname(__file__)

dotenv_path = join(current_dir, '.env')
load_dotenv(dotenv_path)

# DEBUG
DEBUG = os.getenv('DEBUG', 'False')
IS_DEBUG_ENABLED = DEBUG == 'True'

# DATABASE_URI
default_database_path = join(current_dir, 'db', 'battery.db')
DB_PATH = os.getenv('DB_PATH', default_database_path)
DATABASE_URI = f'sqlite:///{DB_PATH}'
