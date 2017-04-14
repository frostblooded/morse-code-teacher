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
        presses = []
        press_start = None
        
        while True:
            # If the input button is pressed and isn't being held
            if GPIO.input(INPUT_BUTTON_PIN) and press_start == None:
                print('Input button pressed')
                press_start = time.time()
            # If the input button isn't pressed and has just been released
            elif not GPIO.input(INPUT_BUTTON_PIN) and press_start != None:
                press_end = time.time()
                press_duration = press_end - press_start
                presses.append(press_duration)
                
                press_start = None
                print("Input button released. It was pressed for {:0.4f}"
                      .format(press_duration))

            if GPIO.input(END_INPUT_BUTTON_PIN):
                print('Ending input')
                break

        return presses
