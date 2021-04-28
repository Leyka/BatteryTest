import os
from os.path import join, dirname
from dotenv import load_dotenv

current_dir = dirname(__file__)

dotenv_path = join(current_dir, '.env')
load_dotenv(dotenv_path)

# DEBUG
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# DATABASE_URI
default_database_uri = join(current_dir, 'battery_test.db')
DATABASE_URI = os.getenv('DATABASE_URI', f'sqlite:///{default_database_uri}')