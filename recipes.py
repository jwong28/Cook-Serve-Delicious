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

def salad(ticket):
    keys = []
    ingredientMap = {
        'Ranch' : 'r',
        'Cheese' : 'c',
        'Thousand' : 't',
        'Vin' : 'v',
        'Bacon' : 'b',
        'Onions' : 'o',
        'Mushrooms' : 'm',
        'Greens' : 'g'
    }
    everythingList = ['b', 'o', 'm', 'g']

    if ('everything' in ticket):
        keys.extend(everythingList)
    for ingredient in list(ingredientMap):
        if (ingredient in ticket):
            keys.append(ingredientMap[ingredient])
    
    for key in keys:
        press(key)
    pressServeCook()

def wine(wineName):
    wineList = ['cheap']
    index = wineList.index(wineName)
    for x in range(index):
        press('q')
    for x in range(27):
        press('w')
    pressServeCook()

