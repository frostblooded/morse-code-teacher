from input_handler import InputHandler

class Program:
    INPUT_BUTTON_PIN = 17
    END_INPUT_BUTTON_PIN = 18

    DOT = 0
    DASH = 1

    DOT_DASH_BORDER = 0.15

    def loop(self):
        presses = self.input_handler.read()
        morse_code = self.input_handler.transform_presses(presses,
                                                    Program.DOT,
                                                    Program.DASH,
                                                    Program.DOT_DASH_BORDER)
        print(morse_code)

    def __init__(self):
        self.input_handler = InputHandler(Program.INPUT_BUTTON_PIN,
                                    Program.END_INPUT_BUTTON_PIN)
        
        while True:
            self.loop()
