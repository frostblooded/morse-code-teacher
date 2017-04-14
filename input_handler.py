import RPi.GPIO as GPIO
import time

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
        pass
        press_start = None
        
        while True:
            if GPIO.input(INPUT_BUTTON_PIN) and press_start == None:
                print('Input button pressed')
                press_start = time.time()
            elif not GPIO.input(INPUT_BUTTON_PIN) and press_start != None:
                press_end = time.time()
                press_duration = press_end - press_start
                press_start = None
                print("Input button released. It was pressed for {:0.4f}"
                      .format(press_duration))

            if GPIO.input(END_INPUT_BUTTON_PIN):
                print('Ending input')
                break
