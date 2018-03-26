# Statement for enabling the development environment
DEBUG = False

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_URL_PATH = "static"

COLORS_CSV_PATH = os.path.join(BASE_DIR, 'colors.csv')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'colors.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

SECRET_KEY = "secret!"

logging_config = {
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'root': {
        'level': 'INFO',
    }
}

