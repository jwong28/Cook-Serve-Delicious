import cv2
import numpy as np
from PIL import ImageGrab, Image, ImageChops
import pytesseract
import time
import pyautogui


from constants import *
from recipes import *
from reader import *
from chores import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

idle_order_nums = [(i) for i in range(AVAILABLE_TICKETS)]
lit_order_nums = []
active_order_nums = []
cooking_order_nums = []
phase2Func = {}

def findAction():
    for i in range(AVAILABLE_TICKETS):
            if (i not in active_order_nums):
                img = ImageGrab.grab(TICKETS_NUM_BOX[i])
                if (checkIfLit(img)):
                    active_order_nums.append(i)

def cook(orderNum, isPhase1):
     result = 0
     title = getTicketTitle()
     text = getTicketText()
    #  print(str(orderNum) + ' Ticket title: ' + title)
     if (title == ''):
        #  print('empty title')
         empty = ImageGrab.grab(TICKET_TITLE_BOX)
         empty.save('empty.png')
         time.sleep(0.5)
         title = getTicketTitle()
        #  print('New ticket title: ' + title)
     if (isChore(title)):
        time.sleep(.3)
        return 2
     if (not isPhase1):
         rec = phase2Func[orderNum]
         result = RECIPE_MULTI_DICT[rec](orderNum + 1, title, text, isPhase1)
         del phase2Func[orderNum]
         if (result > 0):
                pressServeCook()
                return result
    #  recipeFound = False1
     for recipe in AVAILABLE_RECIPES:
            result = 0
            if (recipe in RECIPE_SINGLE_DICT.keys()):
                result = RECIPE_SINGLE_DICT[recipe](orderNum + 1, title, text)
            elif (recipe in RECIPE_MULTI_DICT.keys()):
                result = RECIPE_MULTI_DICT[recipe](orderNum + 1, title, text, isPhase1)
                if (result == 1):
                    phase2Func[orderNum] = recipe
                    # print('Order: ' + str(orderNum) + ' going to phase 2' )
            if (result > 0):
                recipeFound = True
                pressServeCook()
                return result
     # Trouble with salad. If all are not found, has to be salad
    #  if (not recipeFound):
    #     return salad(getTicketText())
     return 4
    # cooking = burger(getTicketText(), isPhase1)
    # pressServeCook()
    # return cooking

def addToCooking(order):
    # lit_order_nums.remove(order)
    cooking_order_nums.append(order) 

def addToLit(order): 
    # idle_order_nums.remove(order)
    lit_order_nums.append(order)

def addToIdle(order):
    pass
    # idle_order_nums.append(order)
    # idle_order_nums.sort()
   
def removeFromCooking(order):
    cooking_order_nums.remove(order)
    # idle_order_nums.append(order)
    # idle_order_nums.sort()
    # print('Order idle: ' + str(order))
   

if __name__ == '__main__': 
    print('hello start')
    threshold = 50
    # print(getButtonText())    
    try: 
        while True:
        # while False:
            for iterations in range(2):
                for cooking_order in range(AVAILABLE_TICKETS):
                    cooking_order_num = cooking_order
                    outline =  ImageGrab.grab(OUTLINE_BOX[cooking_order_num])
                    # Check orders for done cooking
                    if checkIfCooked(outline):
                        print('Order num finshed: ' + str(cooking_order_num + 1))
                        press(str(cooking_order_num + 1))
                        removeFromCooking(cooking_order_num)
                        time.sleep(.2)
                    # Check orders for phase 2
                    if checkIfPhase2(outline):
                        press(str(cooking_order_num + 1))
                        before = ImageGrab.grab(FOOD_BOX)
                        result = cook(cooking_order_num, False)
                        after = ImageGrab.grab(FOOD_BOX)
                        diff = ImageChops.difference(before, after)
                        diff = diff.point(lambda x: 0 if x < threshold else 255)
                        if diff.getbbox() is None or result == 4:
                            time.sleep(.5)
                            after.save('empty.png')
                            print('Order not complete: ' + str(cooking_order_num + 1))
                            cook(cooking_order_num, False)
                        removeFromCooking(cooking_order_num)
                        time.sleep(.2)
            # Check all idle orders
            for awaiting_order in range(AVAILABLE_TICKETS):
                if (awaiting_order not in cooking_order_nums and
                    awaiting_order not in lit_order_nums):
                    awaiting_order_num = awaiting_order
                    img = ImageGrab.grab(TICKETS_NUM_BOX[awaiting_order_num])
                    if checkIfLit(img) :
                        addToLit(awaiting_order_num)
            # if (len(lit_order_nums) > 0):
                # print('lit orders ' + str(lit_order_nums))
            if (len(lit_order_nums) > 0):
                active_order_num = lit_order_nums.pop(0)
                press(str(active_order_num + 1))
                # addToCooking(awaiting_order_num)
                before = ImageGrab.grab(FOOD_BOX)
                cooking = cook(active_order_num, True)
                after = ImageGrab.grab(FOOD_BOX)
                diff = ImageChops.difference(before, after)
                diff = diff.point(lambda x: 0 if x < threshold else 255)
                if diff.getbbox() is None or cooking == 4:
                    time.sleep(.5)
                    after.save('empty.png')
                    print('Order not complete: ' + str(active_order_num + 1))
                    cooking = cook(active_order_num, True)

                if (cooking == 1):
                    addToCooking(active_order_num)
                elif (cooking == 2):
                    addToIdle(active_order_num)
                time.sleep(0.5)

    except KeyboardInterrupt:
        pass
   