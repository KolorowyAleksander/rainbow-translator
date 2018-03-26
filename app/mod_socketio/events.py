from flask import Blueprint, jsonify
from flask_socketio import emit

from app import socketio, logger, app, db
from app.mod_colors.models import Color
from app.devices import sensor

mod_socketio = Blueprint('socketio', __name__, url_prefix='/')


def get_all_colors():
    colors=Color.query.all()
    return [{'rgb': color.rgb, 'color': color.color} for color in colors]


@socketio.on_error()
def error_handler(e):
    logger.exception(e)


@socketio.on('select')
def select(req):
    emit('colors', get_all_colors())


@socketio.on('insert')
def insert(color):
    db.session.add(Color(rgb=color['rgb'], color=color['color']))
    db.session.commit()
    emit('colors', get_all_colors(), broadcast=True)


@socketio.on('delete')
def delete(color):
    color = Color.query.filter(Color.rgb == color['rgb']).first()
    db.session.delete(color)
    db.session.commit()
    emit('colors', get_all_colors(), broadcast=True)


@socketio.on('deleteAll')
def delete_all(req):
    Color.query.delete()
    db.session.commit()
    emit('colors', get_all_colors(), broadcast=True)


@socketio.on('connect')
def socket_connection():
    logger.info('recieved a connection')


@socketio.on('disconnect')
def socket_disconnection():
    logger.info('disconnected')


@socketio.on('click')
def click(message):
    sensor.toggle_light()

