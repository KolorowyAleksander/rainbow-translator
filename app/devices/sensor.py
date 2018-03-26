from Adafruit_TCS34725 import TCS34725, TCS34725_INTEGRATIONTIME_700MS


class TCSSensor():
    def __init__(self):
        self.light_on = True
        self.tcs = TCS34725(integration_time=TCS34725_INTEGRATIONTIME_700MS)

    def get_colors(self):
        r, g, b, _ = self.tcs.get_raw_data()
        return r, g, b

    def toggle_light(self):
        self.light_on = not self.light_on
        self.tcs.set_interrupt(not self.light_on)

sensor = TCSSensor()

