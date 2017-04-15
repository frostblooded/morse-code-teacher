from subprocess import call
from morse_code_transformer import MorseCodeTransformer

class OutputHandler:
    @staticmethod
    def say(something, rate=None): # I'm giving up on you
        args = ['espeak', something]

        if rate:
            args.append('-s')
            args.append(str(rate))
        
        call(args)

    @staticmethod
    def introduce_letter(letter):
        OutputHandler.say('please enter the letter ' + letter)
        morse_letter = MorseCodeTransformer.LETTERS[letter]
        
        symbols = ['dot' if symbol == MorseCodeTransformer.DOT
                   else 'dash'
                   for symbol in morse_letter]
        
        symbols = ' '.join(symbols)
        OutputHandler.say(symbols, 100)
