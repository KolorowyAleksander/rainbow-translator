import csv

import eventlet

from app import socketio, app
from app.devices.matching import closest_color


def measure_colors(socketio, sensor, led):
    colors = None
    with open(app.config['COLORS_CSV_PATH']) as colors_csv:
        colors_reader = csv.reader(colors_csv)
        colors = [tuple(row) for row in colors_reader]

    while True:
        # Run the sensor, light the led and push to all clients
        r, g, b = sensor.get_colors()
        result = '#{0:02x}{1:02x}{2:02x}'.format(r>>8, g>>8, b>>8)

        led.set_color(r>>8, g>>8, b>>8)

        closest = closest_color(result, colors)

        # Sends the color to all clients
        socketio.emit('color', {'color': closest[0], 'rgb': result})
        eventlet.sleep(1)


if app.config['DEBUG']:
    from app.devices.fakeled import led
    from app.devices.mocksensor import sensor
else:
   from app.devices.fakeled import led
   from app.devices.sensor import sensor

