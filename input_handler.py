import RPi.GPIO as GPIO
import time
from input_reader import InputReader

class InputHandler:
    def __init__(self, input_button_pin, end_input_button_pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.input_button_pin = input_button_pin
        self.end_input_button_pin = end_input_button_pin
        
        GPIO.setup(self.input_button_pin, GPIO.IN)
        GPIO.setup(self.end_input_button_pin, GPIO.IN)

    def read(self):
        reader = InputReader(self.input_button_pin, self.end_input_button_pin)
        return reader.read()
            

    def transform_presses(self, presses, dot, dash, dot_dash_border):
        if presses == []:
            return []
        
        return [dot if press < dot_dash_border else dash for press in presses]
