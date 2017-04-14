from input_handler import InputHandler


def loop():
    presses = InputHandler.read()

    for press in presses:
        print(press)

def init():
    InputHandler.init()
    
    while True:
        loop()

if __name__ == '__main__':
    init()
