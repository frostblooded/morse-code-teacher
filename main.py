from input_handler import InputHandler


def loop():
    InputHandler.read()

def init():
    InputHandler.init()
    
    while True:
        loop()

if __name__ == '__main__':
    init()
