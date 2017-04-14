from input_handler import InputHandler

class Program:
    INPUT_BUTTON_PIN = 17
    END_INPUT_BUTTON_PIN = 18

    DOT = 0
    DASH = 1

    def loop(self):
        presses = self.handler.read()
        morse_code = self.handler.transform_presses(presses,
                                                    Program.DOT,
                                                    Program.DASH)
        print(morse_code)

    def __init__(self):
        self.handler = InputHandler(Program.INPUT_BUTTON_PIN,
                                    Program.END_INPUT_BUTTON_PIN)
        
        while True:
            self.loop()
