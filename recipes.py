from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller

import time

keyboard = Controller()

def press(key):
    keyboard.press(key)
    time.sleep(0.05)
    keyboard.release(key)
    time.sleep(0.05)

def pressServeCook():
    press(Key.space)


def chicken():
    for x in range(6):
        press('q')
    press('e')
    pressServeCook()

def wine(wineName):
    wineList = ['cheap']
    index = wineList.index(wineName)
    for x in range(index):
        press('q')
    for x in range(27):
        press('w')
    pressServeCook()
 
if __name__ == "__main__":
    time.sleep(3)
    chicken()

