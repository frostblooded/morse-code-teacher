import RPi.GPIO as GPIO
import time
from input_reader import InputReader

class InputHandler:
    INPUT_BUTTON_PIN = 17
    END_INPUT_BUTTON_PIN = 18
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        GPIO.setup(InputHandler.INPUT_BUTTON_PIN, GPIO.IN)
        GPIO.setup(InputHandler.END_INPUT_BUTTON_PIN, GPIO.IN)

    def read(self):
        reader = InputReader(InputHandler.INPUT_BUTTON_PIN, InputHandler.END_INPUT_BUTTON_PIN)
        return reader.read()
