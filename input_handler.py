import RPi.GPIO as GPIO
import time
from input_reader import InputReader

INPUT_BUTTON_PIN = 17
END_INPUT_BUTTON_PIN = 18

class InputHandler:
    @staticmethod
    def init():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        GPIO.setup(INPUT_BUTTON_PIN, GPIO.IN)
        GPIO.setup(END_INPUT_BUTTON_PIN, GPIO.IN)

    @staticmethod
    def read():
        reader = InputReader(INPUT_BUTTON_PIN, END_INPUT_BUTTON_PIN)
        return reader.read()
