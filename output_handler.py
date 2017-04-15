from subprocess import call
from morse_code_transformer import MorseCodeTransformer

class OutputHandler:
    def say(self, something, rate=None): # I'm giving up on you
        args = ['espeak', something]

        if rate:
            args.append('-s')
            args.append(str(rate))
        
        call(args)
    
    def introduce_letter(self, letter):
        self.say('please enter the letter ' + letter)
        morse_letter = MorseCodeTransformer.LETTERS[letter]
        
        symbols = ['dot' if symbol == MorseCodeTransformer.DOT
                   else 'dash'
                   for symbol in morse_letter]
        
        symbols = ' '.join(symbols)
        self.say(symbols, 100)

    def congratulate(self):
        self.say('well done')
