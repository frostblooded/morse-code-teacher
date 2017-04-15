class MorseCodeTransformer:
    DOT = 0
    DASH = 1

    DOT_DASH_BORDER = 0.30

    LETTERS = {
        'a': [DOT, DASH],
        'b': [DASH, DOT, DOT, DOT],
        'c': [DASH, DOT, DASH, DOT],
        'd': [DASH, DOT, DOT],
        'e': [DOT],
        'f': [DOT, DOT, DASH, DOT],
        'g': [DASH, DASH, DOT],
        'h': [DOT, DOT, DOT, DOT],
        'i': [DOT, DOT],
        'j': [DOT, DASH, DASH, DASH],
        'k': [DASH, DOT, DASH],
        'l': [DOT, DASH, DOT, DOT],
        'm': [DASH, DASH],
        'n': [DASH, DOT],
        'o': [DASH, DASH, DASH],
        'p': [DOT, DASH, DASH, DOT],
        'q': [DASH, DASH, DOT, DASH],
        'r': [DOT, DASH, DOT],
        's': [DOT, DOT, DOT],
        't': [DASH],
        'u': [DOT, DOT, DASH],
        'v': [DOT, DOT, DOT, DASH],
        'w': [DOT, DASH, DASH],
        'x': [DASH, DOT, DOT, DASH],
        'y': [DASH, DOT, DASH, DASH],
        'z': [DASH, DASH, DOT, DOT],
    }

    def from_presses(self, presses):
        if presses == []:
            return []
        
        return [MorseCodeTransformer.DOT
                if press < MorseCodeTransformer.DOT_DASH_BORDER
                else MorseCodeTransformer.DASH
                for press in presses]


    def to_char(self, morse_symbol):
        for character, morse in MorseCodeTransformer.LETTERS.iteritems():      
            if morse == morse_symbol:
                return character

        return ''
        
