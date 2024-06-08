from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller

import time
from reader import *

keyboard = Controller()

def press(key):
    # if (key == ''):
    #     return
    keyboard.press(key)
    time.sleep(0.05)
    keyboard.release(key)
    time.sleep(0.05)

def pressServeCook():
    press(Key.space)

def logCooking(dish, orderNum, title, text, isPhase1 = False):
    log = 'Order ' + str(orderNum) + '   ' + dish + '  ' + str(isPhase1) + '\n  ' \
        + title + '\n  ' + text
    print(log)

# Pytesseract can lead to weird text readings, in these cases
# specific text will be used to determine key to press

# Return 0 if recipe not found
# Return 1 if recipe is cooking
# Return 2 if recipe is served

def attemptSopapillas(orderNum, title, text):
    if (SOPAPILLAS in title):
        return sopapillas(orderNum, title, text)
    return 0
    

def sopapillas(orderNum, title, text):
    logCooking(SOPAPILLAS, orderNum, title, text)
    keyboard.press('q')
    time.sleep(3.25)
    keyboard.release('q')
    time.sleep(.05)
    press('w')
    if ('lite' not in title):
        press('a')
    return 2

def attemptCorndog(orderNum, title, text):
    if ('dog' in title or 'doq' in title or 'do’' in title):
        return corndog(orderNum, title, text)
    return 0

def corndog(orderNum, title, text):
    logCooking(CORNDOG, orderNum, title, text)
    if ('ketchup' in text or 'and' in text):
        press('k')
    if ('mustard' in text):
        press('m')
    return 2

def attemptPretzel(orderNum, title, text):
    if (locateFood(PRETZEL)):
        return pretzel(orderNum, title, text)
    return 0

def pretzel(orderNum, title, text):
    logCooking(PRETZEL, orderNum, title, text)
    if ('cinnamon' in text):
        press('c')
    if ('salt' in text or "“" in text):
        press('s')
    if ('butter' in text or "-" in text):
        press('b')
    return 2

def attemptBeer(orderNum, title, text):
    if ('brewsky' in title):
        return beer(orderNum, title, text)
    return 0

def beer(orderNum, title, text):
    logCooking(BEER, orderNum, title, text)
    keyboard.press('s')
    time.sleep(1.4)
    keyboard.release('s')
    return 2

def attemptFriedChicken(orderNum, title, text):
    if ('fried chicken' in title):
        friedChicken(orderNum, title, text)

def friedChicken(orderNum, title, text):
    logCooking(FRIED_CHICKEN, orderNum, title, text)
    keyboard.press('d')
    time.sleep(3.25)
    keyboard.release('d')
    time.sleep(.05)
    press('b')
    return 2

def attemptSoda(orderNum, title, text):
    if (locateFood('soda')):
        return soda(orderNum, title, text)
    return 0

def soda(orderNum, title, text):
    logCooking(SODA, orderNum, title, text)
    if ('medium' in title):
        press('w')
    elif ('large' in title):
        press('w')
        press('w')
    if ('diet' in title):
        press('a')
    elif ('water' in title):
        press('a')
        press('a')
    elif ('tea' in title):
        press('d')
    elif ('grape' in title):
        press('d')
        press('d')
    if ('ice' not in title):
        press('i')
    press('p')
    return 2

def attemptFries(orderNum, title, text):
    logCooking(FRIES, orderNum, title, text)
    if(FRIES in text):
        return fries(orderNum, title, text)
    return 0
    
def fries(orderNum, title, text):
    keyboard.press('q')
    time.sleep(3.25)
    keyboard.release('q')
    time.sleep(.05)
    press('w')
    if ('sea' in text):
        press('s')
    elif ('salt' in text):
        press('a')
    if ('sugar' in text):
        press('d')
    return 2

def attemptSalad(orderNum, title, text):
    if (locateFood(SALAD)):
        return salad(orderNum, title, text)
    return 0

def salad(orderNum, title, text):
    logCooking(SALAD, orderNum, title, text)
    keys = []
    ingredientMap = {
        'anch' : 'r',
        'eese' : 'c',
        'sand' : 't',
        'ina' : 'v',
        'con' : 'b',
        'ions' : 'o',
        'mush' : 'm',
        'reens' : 'g'
    }
    everythingList = ['b', 'o', 'm', 'g']

    if ('everything' in text):
        keys.extend(everythingList)
    for ingredient in list(ingredientMap):
        if (ingredient in text):
            keys.append(ingredientMap[ingredient])
    
    print(keys)
    for key in keys:
        press(key)
    return 2

def attemptIceCream(orderNum, title, text):
    iceCreamNames = ['vanilla',
                     'chocolate',
                     'yin',
                     'cherry',
                     'sprinkles',
                     'trio',
                     'mint',
                     'nutty',
                     'birthday',
                     'fiesta',
                     'butter pecan',
                     'buttery nuts',
                     ]
    for iceCreamFlavaor in iceCreamNames:
        if (iceCreamFlavaor in title):
            return iceCream(orderNum, title, text)
    return 0

# Brute force for now
def iceCream(orderNum, title, text):
    logCooking(ICE_CREAM, orderNum, title, text)
    keys = []

    if ('plan' in title or 'plain' in title):
        if('vanilla' in title):
            keys = ['q', 'q', 'q']
        elif ('chocolate' in title):
            keys = ['e', 'e', 'e']
    elif ('vanilla and chocolate' in title):
        keys = ['q', 'e']
    elif ('yin' in title):
        keys = ['q', 'e', 'c', 's']
    elif ('cherry vanilla' in title):
        keys = ['q', 'q', 'c']
    elif ('chocolate sprinkles' in title):
        keys = ['e', 'e', 's']
    elif ('trio' in title):
        keys = ['q', 'e', 'a']
    elif ('minty deluxe' in title):
        keys = ['a', 'a', 'c', 'w', 'n']
    elif ('mint cherry' in title):
        keys = ['a', 'a', 'c']
    elif ('nutty mint' in title):
        keys = ['a', 'a', 'n']
    elif ('nutty vanilla' in title):
        keys = ['q', 'q', 'n']
    elif ('nutty chocolate' in title):
        keys = ['e', 'e', 'n']
    elif ('vanilla dream' in title):
        keys = ['q', 'q', 'q', 'c', 's', 'w', 'n', 'o', 'p']
    elif ('chocolate heaven' in title):
        keys = ['e', 'a', 'a', 'c', 's', 'w', 'n', 'o', 'p']
    elif ('deluxe butter pecan' in title):
        keys = ['d', 'd', 'c', 's', 'w', 'n', 'o', 'p']
    elif ('buttery nuts' in title):
        keys = ['d', 'd', 'c', 'w', 'n']
    elif ('birthday' in title):
        keys = ['q', 'e', 'd', 'c', 's', 'w', 'o']
    elif ('fiesta' in title):
        keys = ['e', 'a', 'd', 'c', 's', 'w', 'o', 'p']
    
    print(keys)
    for key in keys:
        press(key)
    return 2

def attemptPotato(orderNum, title, text, isPhase1):
    if (isPhase1 and locateFood('potato_back')):
        logCooking(POTATO, orderNum, title, text, isPhase1)
        return 1
    elif (not isPhase1 and locateFood(POTATO)):
        return potato(text)
    return 0

def potato(orderNum, title, text):
    logCooking(POTATO, orderNum, title, text)
    keys = []

    if ('everything' in text):
        keys = ['c', 's', 'u', 'h', 'b', 'o', 'v', 'i', 'r', 'q', 'm']
        if ('but' in text):
            keys.remove('q')
        elif ('except'):
            keys.remove('c')
    else:
        if ('cheese' in text):
            keys.append('c')
        if ('cream' in text):
            keys.append('s')
        if ('butter' in text):
            keys.append('u')
        if ('chives' in text):
            keys.append('h')
        if ('bacon' in text):
            keys.append('b')
        if ('onions' in text):
            keys.append('o')
        if ('olives' in text):
            keys.append('v')
        if ('spices' in text):
            keys.append('i')
        if ('broccoli' in text):
            keys.append('r')
        if ('queso' in text):
            keys.append('q')
        if ('meats' in text):
            keys.append('m')

    print(keys)
    for key in keys:
        press(key)
    return 2

def attemptNachos(orderNum, title, text, isPhase1):
    if ('ground meat' in getButtonText() or locateFood(NACHOS)):
        return nachos(orderNum, title, text, isPhase1)
    return 0

def nachos(orderNum, title, text, isPhase1):
    logCooking(NACHOS, orderNum, title, text, isPhase1)
    keys = []

    if ('everything' in text):
        keys = ['q', 'c', 'g', 'l', 'j', 't', 'n', 'e', 'i', 'm', 'k', 's', 'b']
    else:
        if ('ground' in text):
            keys.append('m')
        if ('chicken' in text):
            keys.append('k')
        if ('shrimp' in text):
            keys.append('s')
        if ('beef' in text):
            keys.append('b')
        if ('queso' in text):
            keys.append('q')
        if ('cream' in text):
            keys.append('c')
        if ('guac' in text):
            keys.append('g')
        if ('olives' in text):
            keys.append('l')
        if ('jalapenos' in text):
            keys.append('j')
        if ('tomato' in text):
            keys.append('t')
        if ('onions' in text):
            keys.append('n')
        if ('beans' in text):
            keys.append('b')
        if ('rice' in text):
            keys.append('i')

    print(keys)
    for key in keys:
        press(key)
    
    if (('m' in keys or 's' in keys or 'k' in keys or 'b' in keys) and isPhase1):
        return 1
    return 2

def attemptLasagna(orderNum, title, text):
    if (LASAGNA in title):
        return lasagna(orderNum, title, text)
    return 0
     
def lasagna(orderNum, title, text):
    logCooking(LASAGNA, orderNum, title, text)
    keys = []

    if ('tal' in title):
        for i in range(3):
            keys.extend(['q', 'w', 'e', 'r'])
    elif ('meaty' in title):
        for i in range(2):
            keys.extend(['q','w', 'a', 'e', 'r'])
        keys.extend(['q', 'w', 'e', 'r'])
    elif ('vegetable' in title):
        for i in range(2):
            keys.extend(['q','w', 's', 'e', 'r'])
        keys.extend(['q', 'w', 'e', 'r'])
    elif ('piza' in title):
        keys = ['q','w', 'a', 'e', 'r', 'q','w', 's', 'e', 'r', 'q', 'w', 'e', 'r']
    
    for key in keys:
        press(key)
    return 1

def attemptFish(orderNum, title, text):
    if ('rainbow' in title):
    # if ('racc' in title):
        return fish(orderNum, title, text)
    return 0

def fish(orderNum, title, text):
    logCooking(FISH, orderNum, title, text)
    keys = ['a', 's', 'd', 'w']

    if ('lemon' in title):
        keys.append('q')

    print(keys)
    for key in keys:
        press(key)
    return 1

def attemptChickenBreast(orderNum, title, text):
    if ('chicken breast' in title):
        return chickenBreast(orderNum, title, text)
    return 0

def chickenBreast(orderNum, title, text):
    logCooking(CHICKEN, orderNum, title, text)
    keys = ['q', 'q', 'q', 'q', 'q', 'q', 'e']
    for key in keys:
        press(key)
    return 1

def attemptPasta(orderNum, title, text, isPhase1):
    if (PASTA in text):
        return pasta(orderNum, title, text, isPhase1)
    elif (not isPhase1):
        return pasta(orderNum, title, text, isPhase1)
    return 0

def pasta(orderNum, title, text, isPhase1):
    logCooking(PASTA, orderNum, title, text, isPhase1)
    keys = []
    if (isPhase1):
        press('q')
        return 1
    else:
        if ('all top' in text):
            keys = ['m', 'k', 'b', 'p', 'u', 's', 'o', 'i', 't']
        else:
            if ('meatballs' in text):
                keys.append('m')
            if ('chicken' in text):
                keys.append('k')
            if ('bacon' in text):
                keys.append('b')
            if ('red pepper' in text):
                keys.append('p')
            if ('mushrooms' in text):
                keys.append('u')
            if ('spinach' in text):
                keys.append('s')
            if ('onions' in text):
                keys.append('o')
            if ('spices' in text):
                keys.append('i')
            if ('tomato' in text):
                keys.append('t')
        if ('cheese' in text):
            keys.append('c')
        if ('red sauce' in text):
            keys.append('r')
        if ('white' in text):
            keys.append('w')
        if ('green' in text):
            keys.append('g')    

    print(keys)
    for key in keys:
        press(key)
    return 2

def attemptWine(orderNum, title, text):
    if ('bottle' in text or 'rattle' in text):
        return wine(orderNum, title, text)
    return 0

# For some reason, elk cannot be read
def wine(orderNum, title, text):
    logCooking(WINE, orderNum, title, text)
    keys = []
    wineList = ['cheap', 'marzu', 'serpent', '', 'deckard']
    if ('cheap' in title):
        pass
    elif ('marzu' in title):
        keys.extend(['q'])
    elif ('beard' in title):
        keys.extend(['q', 'q'])
    elif ('deckard' in title):
        keys.extend(['q', 'q', 'q', 'q'])
    else: 
        keys.extend(['q', 'q', 'q'])
    for x in range(27):
        keys.append('w')
    for key in keys:
        press(key)
    return 2

def attemptPizza(orderNum, title, text):
    possible_text = [PIZZA, 'pesto p', 'cheesy bread', 'veggie p']
    for possible in possible_text:
        if (possible in title):
            if (possible == 'cheesy bread' and 'the' in title):
                return 0
    # if (PIZZA in title or locateFood(PIZZA)):
            return pizza(orderNum, title, text)
    return 0

def pizza(orderNum, title, text):
    logCooking(PIZZA, orderNum, title, text)
    keys = []

    if ('tomato sauce' in text):
        keys.append('q')
    elif ('pesto' in text):
        keys.append('e')
    if ('everything' in text):
        keys.extend(['c', 'p', 's', 'b', 'a', 'h', 'm', 'l', 'n', 'i', 't'])
        if ('but' in text):
            keys.remove('t')
    else:
        if ('chees' in text):
            keys.append('c')
        if ('pepperoni' in text or 'eron' in text):
            keys.append('p')
        if ('sausage' in text):
            keys.append('s')
        if ('bacon' in text):
            keys.append('b')
        if ('anchovies' in text):
            keys.append('a')
        if ('ham' in text):
            keys.append('h')
        if ('mushrooms' in text):
            keys.append('m')
        if ('olives' in text):
            keys.append('l')
        if ('onions' in text):
            keys.append('n')
        if ('apple' in text):
            keys.append('i')
        if ('tomatoes' in text):
            keys.append('t')

    print(keys)
    for key in keys:
        press(key)
    return 1

def attemptBurger(orderNum, title, text, isPhase1):
    buttonText = getButtonText()
    if (('eat' in buttonText or 'eet' in buttonText) and 
        'ground' not in getButtonText()):
        return burger(orderNum, title, text, isPhase1)
    elif (not isPhase1):
        return burger(orderNum, title, text, isPhase1)
    return 0

def burger(orderNum, title, text, isPhase1):
    logCooking(BURGER, orderNum, title, text, isPhase1)
    keys = []
    count = 0

    if (isPhase1):
        if ("one" in text and "everything" not in text):
            count = 1
        if ("two" in text):
            count = 2
        elif ('three' in text):
            count = 3
        if ('meat' in text):
            for i in range(count):
                keys.append('m')
        if ('chicken' in text):
            for i in range(count):
                keys.append('k')
    if (count == 0): 
        if ('everything' in text):
            keys = ['m', 'k', 'l', 'b', 'c', 't', 'p', 'o', 's']
        else:
            if ('meat' in text):
                keys.append('m')
                if ('meat (2x)' in text):
                    keys.append('m')
                if ('meat (3x)' in text):
                    keys.extend(['m', 'm'])
            if ('chicken' in text):
                keys.append('k')
                if ('chicken (2x)' in text):
                    keys.append('k')
            if ('cheese' in text and
                'swiss' in text):
                cheeseLoc = text.find('cheese')
                swissLoc = text.find('swiss')
                if (swissLoc > cheeseLoc):
                    keys.extend(['s', 'c'])
                else:
                    keys.append('s')
            elif ('cheese' in text):
                keys.append('c')
                if ('cheese (2x)' in text):
                    keys.append('c')
            if ('lettuce' in text):
                keys.append('l')
            if ('bacon' in text):
                keys.append('b')
                if ('bacon (2x)' in text):
                    keys.append('b')
            if ('tomato' in text):
                keys.append('t')
            if ('pickles' in text):
                keys.append('p')
            if ('onions' in text):
                keys.append('o')

    print(keys)
    for key in keys:
        press(key)
    
    if (('m' in keys or 'k' in keys) and count > 0):
        return 1
    return 2

def attemptSteak(orderNum, title, text):
    if (STEAK in title or 'bacones' in title):
        return steak(orderNum, title, text)
    return 0

# Brute force for now
def steak(orderNum, title, text):
    logCooking(STEAK, orderNum, title, text)
    keys = []
    if ("classic" in title):
        keys = ['s', 's', 's', 'j']
    elif ("citrus" in title):
        keys = ['s', 'j', 'j', 'c']
    elif ("dry spicy" in title):
        keys = ['s', 'p', 'p']
    elif ("spicy bacones" in title):
        keys = ['s', 'j', 'p', 'p', 'b' ,'b']
    elif ("bacones" in title):
        keys = ['s', 'j', 'j', 'b' ,'b']
    elif ("spicy smokey" in title):
        keys = ['s', 's', 'd', 'p', 'p', 'p', 'j', 'j']
    elif ("smokey orange" in title):
        keys = ['s', 'd', 'j', 'c', 'c']
    elif ("hickory" in title):
        keys = ['s', 's', 'h', 'h', 'j', 'j', 'j', 'j']
    elif ("spicy" in title):
        keys = ['s', 'p', 'p' ,'p', 'p', 'j', 'j']
    elif ("texas" in title):
        keys = ['s', 's', 'h', 'h', 'j', 'j', 'b', 'b', 'd', 'd', 'p', 'p']

    print(keys)
    for key in keys:
        press(key)
    return 1

def attemptSoup(orderNum, title, text):
    if (SOUP in title or 'stew' in title or locateFood('soup')):
        return soup(orderNum, title, text)
    return 0

def soup(orderNum, title, text):
    logCooking(SOUP, orderNum, title, text)
    keys = []

    if ('chicken' in text):
        keys.append('k')
    if ('meats' in text):
        keys.append('m')
    if ('rice' in text):
        keys.append('i')
    if ('ham' in text):
        keys.append('h')
    if ('bowtie' in text):
        keys.append('w')
    if ('illon' in text):
        keys.append('u')
    if ('seasoning' in text):
        keys.append('s')
    if ('potato' in text):
        keys.append('p')
    if ('bacon' in text):
        keys.append('b')
    if ('cheese' in text):
        keys.append('c')
    if ('red pepper' in text):
        keys.append('d')
    if ('garl' in text or 'carl' in text):
        keys.append('g')
    if ('beans' in text):
        keys.append('e')
    if ('onions' in text):
        keys.append('n')
    if ('broccoli' in text):
        keys.append('r')
    if ('tomato' in text):
        keys.append('t')
        soupChop(keys)
    if ('carrot' in text):
        keys.append('a')
        soupChop(keys)
    if ('celery' in text):
        keys.append('y')
        soupChop(keys)
    if ('cabbage' in text):
        keys.append('j')
        soupChop(keys)
    if ('zucchini' in text):
        keys.append('z')
        soupChop(keys)

    print(keys)
    for key in keys:
        press(key)
    return 1

def soupChop(keys):
    return keys.extend(['q', 'q', 'q', 'q', 'q'])

def attemptCoffee(orderNum, title, text):
    if (COFFEE in title or COFFEE in text):
        return coffee(orderNum, title, text)
    return 0

def coffee(orderNum, title, text):
    logCooking(COFFEE, orderNum, title, text)
    keys = []
    sugars = 0
    keys.append(Key.down)
    if ('sug' in title):
        sugars = handleCount(text)
    elif ('loaded' in title):
        keys.append('c')
        sugars =  handleCount(text)
    elif ('cream' in title):
        keys.append('c')

    for i in range(sugars):
            keys.append('s')  

    print(keys)
    for key in keys:
        press(key)
    return 2

def handleCount(text):
    counts = 0
    if ('2' in text):
        counts = 2
    elif ('3' in text):
        counts = 3
    elif ('4' in text):
        counts = 4
    elif ('5' in text):
        counts = 5
    elif ('1' in text or 'l' in text):
        counts = 1
    # print(text + ': ' + str(counts))
    return counts

def attemptHashBrown(orderNum, title, text):
    if ('hash' in title):
        return hashBrown(orderNum, title, text)
    return 0
    

def hashBrown(orderNum, title, text):
    logCooking(HASHBROWN, orderNum, title, text)
    keyboard.press(Key.down)
    time.sleep(2)
    keyboard.release(Key.down)
    time.sleep(.05)
    press('p')
    if ('lite' not in title):
        press('s')
    return 2

def attemptBreakwich(orderNum, title, text):
    if ('cheese' in getButtonText()):
        return breakwich(orderNum, title, text)
    return 0

def breakwich(orderNum, title, text):
    logCooking(BREAKWICH, orderNum, title, text)
    keys = []

    if ('everything' in text):
        keys = ['e', 's', 'b', 'c', 'h']
    else:
        if ('egg' in text or '99' in text):
            keys.append('e')
        if ('sausage' in text):
            keys.append('s')
        if ('bacon' in text):
            keys.append('b')
        if ('cheese' in text):
            keys.append('c')
        if ('ham' in text):
            keys.append('h')

    print(keys)
    for key in keys:
        press(key)
    return 1

def attemptPancake(orderNum, title, text, isPhase1):
    if ('pancake' in getButtonText() or not isPhase1):
        return pancake(orderNum, title, text, isPhase1)
    return 0

def pancake(orderNum, title, text, isPhase1):
    keys = []

    logCooking(PANCAKE, orderNum, title, text, isPhase1)
    if ('one' in text):
        keys = ['p']
    elif ('two' in text):
        keys = ['p', 'p']
    elif ('three' in text):
        keys = ['p', 'p', 'p']
    if (not isPhase1):
        if ('maple' in text):
            keys.append('m')
        elif ('straw' in text):
            keys.append('s')
        elif ('blue' in text):
            keys.append('l')
        elif ('can' in text):
            keys.append('e')
        if ('but' in text and 'no' not in text):
            keys.append('b')

    print(keys)
    for key in keys:
        press(key)
    return 1 if isPhase1 else 2

def attemptSushi(orderNum, title, text):
    if ('yellow' in getButtonText()):
        return sushi(orderNum, title, text)
    return 0

def sushi(orderNum, title, text):
    logCooking(SUSHI, orderNum, title, text)
    keys = []
    items = text.split(',')

    for item in items:
       count = handleCount(item)
       for i in range(count):
            if ('ebi' in item):
               keys.append('e')
            if ('roe' in item):
               keys.append('r')
            if ('oro' in item):
               keys.append('o')
            if ('tuna' in item):
               keys.append('t')
            if ('sal' in item):
               keys.append('s')
            if ('mack' in item):
               keys.append('m')
            if ('yell' in item):
               keys.append('y')
            if ('unag' in item):
               keys.append('g')

    print(keys)
    for key in keys:
        press(key)
    return 2

def attemptFriedRice(orderNum, title, text):
    if ('rice' in title):
        return friedRice(orderNum, title, text)
    return 0

def friedRice(orderNum, title, text):
    logCooking(FRIED_RICE, orderNum, title, text)
    keys = []

    if ('fried' in text):
        keys.append('f')
    elif ('white' in text):
        keys.append('w')
    elif ('brown' in text):
        keys.append('b')
    if ('everything' in text):
        keys.extend(['p', 'c', 'e', 'o', 'n', 'r', 's', 'm', 'k'])
        if ('but' in text):
            keys.remove('s')
    else:
        if ('peas' in text):
            keys.append('p')
        if ('car' in text):
            keys.append('c')
        if ('egg' in text or '99' in text):
            keys.append('e')
        if ('ion' in text):
            keys.append('o')
        if ('bab' in text):
            keys.append('n')
        if ('cco' in text):
            keys.append('r')
        if ('shrimp' in text):
            keys.append('s')
        if ('beef' in text):
            keys.append('m')
        if ('chicken' in text):
            keys.append('k')

    print(keys)
    for key in keys:
        press(key)
    return 1

def attemptLobster(orderNum, title, text, isPhase1):
    if ('a com.' in getButtonText() or not isPhase1):
        return lobster(orderNum, title, text, isPhase1)
    return 0

def lobster(orderNum, title, text, isPhase1):
    keys = []

    logCooking(LOBSTER, orderNum, title, text, isPhase1)
    if (isPhase1):
        keys.append('q')
    else:
        count = 1
        if ('two' in text):
            count = 2
        if (not isPhase1):
            if ('utt' in text):
                keys.append('b')
            if ('tai' in text):
                keys.append('c')
            if ('rli' in text):
                keys.append('g')
            if ('ing' in text):
                keys.append('i')
            if ('icy' in text):
                keys.append('s')
        if (count == 2):
            keys.extend(keys)

    print(keys)
    for key in keys:
        press(key)
    return 1 if isPhase1 else 2

def attemptBananas(orderNum, title, text):
    if (BANANAS in title):
        return bananas(orderNum, title, text)
    return 0

def bananas(orderNum, title, text):
    logCooking(BANANAS, orderNum, title, text)
    press('q')
    press('w')
    time.sleep(2)
    press('e')
    if ('flam' in title):
        press('s')
        press('d')
    return 1  

def attemptKabob(orderNum, title, text):
    if ('kabo' in title):
        return kabob(orderNum, title, text)
    return 0

def kabob(orderNum, title, text):
    keys = []
    logCooking(KABOB, orderNum, title, text)

    if('classic' in title):
        keys = ['t', 'm', 't', 'k', 'g', 'r', 'g', 'r']
    elif('meaty' in title):
        keys = ['t', 'm', 'k', 'm', 'k', 'm', 'k', 'g']
    elif('pepper' in title):
        keys = ['t', 'm', 'g', 'r', 'g', 'r', 'g', 'r']
    elif('red' in title):
        keys = ['t', 'r', 'm', 'r', 't', 'g', 't', 'r']
    elif('kabobber' in title):
        keys = ['t', 'm', 'k', 't', 'm', 'k', 'g', 'r']
    elif('chicken' in title):
        keys = ['t', 'k', 't', 'k', 'g', 'k', 'r', 'k']
    elif('onion' in title):
        keys = ['t', 'o', 'k', 'o', 'g', 'o', 'r', 'o']
    elif('tower' in title):
        keys = ['m', 'k', 'g', 'r', 'o', 'g', 'r', 'o']
    elif('tangy' in title):
        keys = ['t', 'o', 'g', 'r', 'o', 'g', 'r', 'o']
    elif('juicy' in title):
        keys = ['m', 'o', 'k', 'g', 'o', 'm', 'o', 'k']
    elif('hawaii' in title):
        keys = ['t', 'm', 'k', 'p', 'k', 'o', 'p', 'o']
    elif('pine' in title):
        keys = ['t', 'p', 'm', 'p', 'k', 'p', 'o', 'p']
    elif('ombe' in title):
        keys = ['m', 'p', 'm', 'p', 'k', 'g', 'r', 'o']
    elif('sampler' in title):
        keys = ['t', 'k', 'm', 'g', 'r', 'p', 'o', 'p']
    elif('squash' in title):
        keys = ['s', 'g', 's', 'r', 'p', 's', 'o', 'p']
    elif('yellow' in title):
        keys = ['m', 'k', 'p', 's', 'p', 's', 'p', 's']
    elif('crazy' in title):
        keys = ['t', 'k', 'g', 'o', 's', 'g', 'o', 's']
    elif('platt' in title):
        keys = ['t', 'k', 'g', 'k', 'r', 'o', 'p' , 's']
    elif('veggie' in title):
        keys = ['t', 'g', 'o', 'z', 'u', 'o', 'z', 'u']
    elif('america' in title):
        keys = ['k', 'm', 'r', 'o', 's', 'u', 's', 'u']
    elif('green' in title):
        keys = ['k', 'g', 'z', 'u', 'k', 'g', 'z', 'u']
    elif('odessa' in title):
        keys = ['m', 'z', 'm', 'z', 'm', 'z', 's', 'u']
    elif('speci' in title):
        keys = ['t', 'g', 'p', 'u', 't', 'g', 'p', 'u']
    elif('omato' in title):
        keys = ['t', 'm', 't', 'k', 't', 'u', 'z', 'u']

    print(keys)
    for key in keys:
        press(key)
    return 1

def attemptEnchilada(orderNum, title, text):
    if ('ror chives' in getButtonText()):
        return enchilada(orderNum, title, text)
    return 0

def enchilada(orderNum, title, text):
    keys = []
    logCooking(ENCHILADA, orderNum, title, text)

    count = 1
    if ('doub' in text or 'two' in text):
        count = 2
    elif ('trip' in text or 'thr' in text):
        count = 3
    for i in range(count):
        keys.extend([Key.down, Key.up, 't'])
    if ('everything' in text):
        keys.extend(['c', 'e', 'o'])
    else:
        if ('chive' in text):
            keys.append('c')
        if ('egg' in text or '99' in text):
            keys.append('e')
        if ('ion' in text):
            keys.append('o')

    print(keys)
    for key in keys:
        press(key)
    return 2
    

RECIPE_SINGLE_DICT = {
    SOPAPILLAS: attemptSopapillas,
    CORNDOG: attemptCorndog,
    PRETZEL: attemptPretzel,
    BEER: attemptBeer,
    FRIED_CHICKEN: attemptFriedChicken,
    SODA: attemptSoda,
    FRIES: attemptFries,
    SALAD: attemptSalad,
    ICE_CREAM: attemptIceCream,
    LASAGNA: attemptLasagna,
    FISH: attemptFish,
    CHICKEN: attemptChickenBreast,
    WINE: attemptWine,
    PIZZA: attemptPizza,
    STEAK: attemptSteak,
    SOUP: attemptSoup,
    COFFEE: attemptCoffee,
    HASHBROWN: attemptHashBrown,
    BREAKWICH: attemptBreakwich,
    SUSHI: attemptSushi,
    FRIED_RICE: attemptFriedRice,
    BANANAS: attemptBananas,
    KABOB: attemptKabob,
    ENCHILADA: attemptEnchilada,
}

RECIPE_MULTI_DICT = {
    POTATO: attemptPotato,
    NACHOS: attemptNachos,
    PASTA: attemptPasta,
    BURGER: attemptBurger,
    PANCAKE: attemptPancake,
    LOBSTER: attemptLobster,
}