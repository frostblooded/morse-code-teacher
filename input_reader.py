import time
import RPi.GPIO as GPIO

class InputReader:
    def __init__(self, input_button_pin, end_input_button_pin):
        self.input_button_pin = input_button_pin
        self.end_input_button_pin = end_input_button_pin
        self.presses = []
        self.press_start = None

    def handle_just_pressed(self):
        print('Input button pressed')
        self.press_start = time.time()

    def handle_just_released(self):
        press_end = time.time()
        press_duration = press_end - self.press_start
        self.presses.append(press_duration)
        
        self.press_start = None
        print("Input button released. It was pressed for {:0.4f}"
              .format(press_duration))
    
    def read(self):   
        presses = []
        press_start = None
        
        while True:
            if GPIO.input(self.input_button_pin) and self.press_start == None:
                self.handle_just_pressed()
            elif not GPIO.input(self.input_button_pin) and self.press_start != None:
                self.handle_just_released()
            elif GPIO.input(self.end_input_button_pin):
                print('Ending input')
                break

        return self.presses
