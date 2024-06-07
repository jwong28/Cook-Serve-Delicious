from pynput.keyboard import Key, Controller

from reader import *
from constants import *

keyboard = Controller()

def press(key):
    keyboard.press(key)
    time.sleep(0.05)
    keyboard.release(key)
    time.sleep(0.05)

def slowPress(key):
    keyboard.press(key)
    time.sleep(0.15)
    keyboard.release(key)
    time.sleep(0.15)

def isChore(ticket):
    if ('work' in ticket or 'nork' in ticket):
        if ('dishes' in ticket):
            cleanDishes()
            return True
        elif ('clean' in ticket):
            cleanToilet()
            return True
        elif ('trash' in ticket):
            cleanTrash()
            return True
        elif ('rodent' in ticket):
            cleanRodent()
            return True
    elif ('robbery' in ticket):
        getRobber()
        return True
    elif ('my picture' in ticket):
        press('q')
        return True
    elif ('sweetie' in ticket):
        date()
        return True
    return False

def cleanDishes():
    sequences = 3 if UPGRADE_DISH else 3
    if UPGRADE_DISH:
        for i in range(sequences):
            press('a')
            press('d')
            press('w')
    else:
        for i in range(sequences):
            press('a')
            press('d')
            press('a')
            press('d')
            press('w')

def cleanTrash():
    sequences = 2 if UPGRADE_TRASH else 5
    for i in range(sequences):
        slowPress('a')
        slowPress('d')
        if (i < sequences - 1):
            time.sleep(.5)
    press('w')
    press('w')

def cleanToilet():
    press('q')
    press('w')

def cleanRodent():
    press('q')
    press('w')
    press('e')
    press('r')

def getRobber():
    keys = []
    ticket = getTicketText()
    if ('sexy robber' in ticket):
        ticket += ' sexy hair, sexy lips'

    # Hair
    if ('bald' in ticket):
        keys.extend(['h'])
    elif ('sexy hair' in ticket):
        keys.extend(['h', 'h'])
    elif ('spiked hair' in ticket):
        keys.extend(['h', 'h', 'h'])
    elif ('poofy hair' in ticket):
        keys.extend(['h', 'h', 'h', 'h'])

    # Eyes
    if ('normal eyes' in ticket):
        keys.extend(['i'])
    elif ('crazy eyes' in ticket):
        keys.extend(['i', 'i'])
    elif ('sexy eyes' in ticket):
        keys.extend(['i', 'i', 'i'])
    elif ('beady eyes' in ticket):
        keys.extend(['i', 'i', 'i', 'i'])

    # Ears
    if ('normal ears' in ticket):
        keys.extend(['e'])
    elif ('round' in ticket):
        keys.extend(['e', 'e'])
    elif ('long ears' in ticket):
        keys.extend(['e', 'e', 'e'])
    elif ('tiny ears' in ticket or 'ting ears' in ticket):
        keys.extend(['e', 'e', 'e', 'e'])

    # Nose
    if ('crooked nose' in ticket):
        keys.extend(['n'])
    elif ('normal nose' in ticket or 'normal ears/nose' in ticket):
        keys.extend(['n', 'n'])
    elif ('fancy' in ticket and 'nose' in ticket):
        keys.extend(['n', 'n', 'n'])

    # Lips
    if ('long lips' in ticket):
        keys.extend(['l'])
    elif ('small lips' in ticket):
        keys.extend(['l', 'l'])
    elif ('sexy lips' in ticket):
        keys.extend(['l', 'l', 'l'])

    # Beard
    if ('beard' in ticket and 'mustache' in ticket):
        keys.extend(['f', 'f', 'f', 'f'])
    elif ('mustache' in ticket):
        keys.extend(['f'])
    elif ('beard' in ticket):
        keys.extend(['f', 'f'])
    elif ('fuzz' in ticket):
        keys.extend(['f', 'f', 'f'])
    
    keys.append(Key.space)
    for key in keys:
        press(key)


def date():
    print('on date')
    while('sweetie' in getTicketTitle()):
        time.sleep(1)
        # press('w')
    print('done date')