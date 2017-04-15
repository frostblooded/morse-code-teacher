from input_handler import InputHandler
from morse_code_transformer import MorseCodeTransformer
import pyttsx

class Program:
    def loop(self):
        self.speak_engine.say('please enter the letter ' + self.current_letter)
        self.speak_engine.runAndWait()
        presses = self.input_handler.read()
        morse_code = self.transformer.from_presses(presses)
        char = self.transformer.to_char(morse_code)

        if char == self.current_letter:
            if char == 'z':
                self.speak_engine.say('well done!')
                self.speak_engine.runAndWait()
                self.current_letter = 'a'
            else:
                self.current_letter = chr(ord(self.current_letter) + 1)

    def __init__(self):
        self.input_handler = InputHandler()
        self.transformer = MorseCodeTransformer()
        self.speak_engine = pyttsx.init()
        self.current_letter = 'z'
        
        while True:
            self.loop()
