class FakeLed():
    """This can be used if the device is not present"""
    def __init__(self, pins: tuple, started=True, mode=''):
        pass

    def start_pwm(self):
        pass

    def stop_pwm(self):
        pass

    def set_color(self, r, g, b):
        pass

led = FakeLed(())

