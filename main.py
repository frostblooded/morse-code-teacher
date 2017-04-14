import RPi.GPIO as GPIO
import time

INPUT_BUTTON_PIN = 17
END_INPUT_BUTTON_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(INPUT_BUTTON_PIN, GPIO.IN)
GPIO.setup(END_INPUT_BUTTON_PIN, GPIO.IN)

while True:
    if GPIO.input(INPUT_BUTTON_PIN):
        print('Input button pressed!')

    if GPIO.input(END_INPUT_BUTTON_PIN):
        print('End input button pressed!')
