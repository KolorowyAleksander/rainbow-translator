import eventlet
eventlet.monkey_patch()  # required for server to run properly

from app import app, socketio
from app.devices import measure_colors, sensor, led


if __name__ == '__main__':
    # run the sensor and led control in a separate coroutine
    eventlet.spawn(measure_colors, socketio, sensor, led)

    # Without this websocket cannot be used
    socketio.run(app, host='0.0.0.0', port=80, log_output=True)

