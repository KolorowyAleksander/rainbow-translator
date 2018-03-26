from Adafruit_GPIO import PWM
from RPi import GPIO


class RGBLed():
    """
    This class represents an RGB led controlled via pwm on 3 GPIO pins.
    """
    def __init__(self, pins: tuple, started=True, mode=GPIO.BOARD):
        """
        Pins are 3 pin numbers, one for each color on the rgb led
        If started is `False` then `start_pwm` needs to be called
        Mode can be RPi.GPIO.BOARD or RPi.GPIO.BCM
        """
        self.red_pin, self.green_pin, self.blue_pin = pins
        self.pwm = PWM.get_platform_pwm(mode=mode)
        if started:
            self.start_pwm()

    def __del__(self):
        self.stop_pwm()

    def start_pwm(self):
        """
        Start the pwm and turn off the diode
        """
        self.pwm.start(self.red_pin, 100)
        self.pwm.start(self.green_pin, 100)
        self.pwm.start(self.blue_pin, 100)

    def stop_pwm(self):
        """
        Turn off the pwm on the diode
        """
        self.pwm.stop(self.red_pin)
        self.pwm.stop(self.green_pin)
        self.pwm.stop(self.blue_pin)

    def set_color(self, r, g, b):
        """
        r,g,b is expected to be 6 hexes long (html color)
        """
        r, g, b = 100 - r/2.56, 100 - g/2.56, 100 - b/2.56

        self.pwm.set_duty_cycle(self.red_pin, r)
        self.pwm.set_duty_cycle(self.green_pin, g)
        self.pwm.set_duty_cycle(self.blue_pin, b)

led = RGBLed((11, 13, 15))

