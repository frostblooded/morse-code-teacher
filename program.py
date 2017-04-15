from input_handler import InputHandler
from morse_code_transformer import MorseCodeTransformer

class Program:
    def loop(self):
        presses = self.input_handler.read()
        morse_code = self.transformer.from_presses(presses)
        char = self.transformer.to_char(morse_code)
        print(char)

    def __init__(self):
        self.input_handler = InputHandler()
        self.transformer = MorseCodeTransformer()
        
        while True:
            self.loop()
