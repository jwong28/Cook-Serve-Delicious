from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller

import time

keyboard = Controller()

def chicken():
    for x in range(6):
        keyboard.press('q')
        time.sleep(0.05)
    keyboard.press(Key.space)

if __name__ == "__main__":
    chicken()

