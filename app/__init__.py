from logging.config import dictConfig

from flask import Flask, render_template, Blueprint
from flask_restless import APIManager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from config import logging_config

# initiating a basic logger
dictConfig(logging_config)

# Define application object
app = Flask(__name__)

# Define logger
logger = app.logger

# Configurations
app.config.from_object('config')

# SocketIO
socketio = SocketIO(app)

# Database
db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Static files for development
static = Blueprint('static', __name__, static_folder='static', static_url_path='static')

# Load blueprints
from app.mod_colors.controllers import mod_colors as colors_module
from app.mod_socketio.events import mod_socketio as socketio_module

app.register_blueprint(colors_module)
app.register_blueprint(socketio_module)

# create DB
from app.mod_colors.models import Color

db.create_all()

