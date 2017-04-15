from input_handler import InputHandler
from morse_code_transformer import MorseCodeTransformer

class Program:
    def loop(self):
        presses = self.input_handler.read()
        morse_code = self.transformer.from_presses(presses)
        print(morse_code)

    def __init__(self):
        self.input_handler = InputHandler()
        self.transformer = MorseCodeTransformer()
        
        while True:
            self.loop()
