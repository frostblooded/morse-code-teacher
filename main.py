from input_handler import InputHandler


def loop():
    presses = InputHandler.read()

def init():
    InputHandler.init()
    
    while True:
        loop()

if __name__ == '__main__':
    init()
