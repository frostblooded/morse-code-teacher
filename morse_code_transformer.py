class MorseCodeTransformer:
    DOT = 0
    DASH = 1

    DOT_DASH_BORDER = 0.15

    def from_presses(self, presses):
        if presses == []:
            return []
        
        return [MorseCodeTransformer.DOT
                if press < MorseCodeTransformer.DOT_DASH_BORDER
                else MorseCodeTransformer.DASH
                for press in presses]
