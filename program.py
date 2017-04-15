from input_handler import InputHandler
from morse_code_transformer import MorseCodeTransformer
from output_handler import OutputHandler

class Program:
    FIRST_CHAR = 'a'
    LAST_CHAR = 'z'
    
    def loop(self):
        self.output_handler.introduce_letter(self.current_letter)
        presses = self.input_handler.read()
        morse_code = self.transformer.from_presses(presses)
        char = self.transformer.to_char(morse_code)

        if char == self.current_letter:
            if char == Program.LAST_CHAR:
                self.output_handler.congratulate()
                self.current_letter = Program.FIRST_CHAR
            else:
                self.current_letter = chr(ord(self.current_letter) + 1)

    def __init__(self):
        self.input_handler = InputHandler()
        self.transformer = MorseCodeTransformer()
        self.output_handler = OutputHandler()
        self.current_letter = Program.FIRST_CHAR
        
        while True:
            self.loop()
