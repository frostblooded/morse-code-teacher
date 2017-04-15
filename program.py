from input_handler import InputHandler
from morse_code_transformer import MorseCodeTransformer
from output_handler import OutputHandler

class Program:
    FIRST_CHAR = 'a'
    LAST_CHAR = 'z'
    
    def loop(self):
        OutputHandler.introduce_letter(self.current_letter)
        presses = self.input_handler.read()
        morse_code = self.transformer.from_presses(presses)
        char = self.transformer.to_char(morse_code)

        if char == self.current_letter:
            OutputHandler.say('well done')
            
            if char == Program.LAST_CHAR:
                OutputHandler.say('again')
                self.current_letter = Program.FIRST_CHAR
            else:
                self.current_letter = chr(ord(self.current_letter) + 1)
        else:
            OutputHandler.say('wrong')

    def __init__(self):
        self.input_handler = InputHandler()
        self.transformer = MorseCodeTransformer()
        self.current_letter = Program.FIRST_CHAR
        
        while True:
            self.loop()
