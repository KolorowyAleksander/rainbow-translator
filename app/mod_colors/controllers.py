from flask import Blueprint, render_template, jsonify, request

from app import logger, db
from app.mod_colors.models import Color

mod_colors = Blueprint('colors', __name__)


@mod_colors.route('/')
def index():
    logger.info('serving index.html')
    return render_template('colors/index.html')


@mod_colors.route('/version', methods=['GET'])
def version():
    version_info = {
        'version': '1.0.0',
        'name': 'reinbowtranslator'
    }
    return jsonify(version_info)
