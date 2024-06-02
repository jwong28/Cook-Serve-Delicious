import cv2
import numpy as np
from PIL import ImageGrab, Image
import pytesseract
import time
import pyautogui


import constants
import recipes
import task_finder

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

active_order_nums = []
cooking_oerder_nums = []

def imageToText(img):
    # Convert to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get the binary mask
    msk = cv2.inRange(hsv, np.array([0, 0, 0]), np.array([179, 255, 154]))

    # Extract
    krn = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
    dlt = cv2.dilate(msk, krn, iterations=5)
    res = 255 - cv2.bitwise_and(dlt, msk)

    # OCR
    txt = pytesseract.image_to_string(res, config="--psm 6")
    print('hello ' + txt)
    return txt

def getTicketText():
    im = ImageGrab.grab(constants.TICKET_TEXT_BOX)
    img = np.array(im.convert('RGB'))
    return imageToText(img)

def colorExist(img, colors):
    width, height = img.size
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            if ((r, g, b) in colors):
                return True
    return False

def checkIfLit():
    colorExist(img, [constants.AVAIALABLE_ORDER_RGB])

def findAction():
    for i in range(constants.AVAILABLE_TICKETS):
            if (i not in active_order_nums):
                img = ImageGrab.grab(constants.TICKETS_NUM_BOX[i])
                if (checkIfLit(img)):
                    active_order_nums.append(i)

if __name__ == '__main__': 
    time.sleep(2)
    print('hello start')
    # im = ImageGrab.grab()
    # im.save('temp1.png')
    # im = Image.open('temp1.png')
    # img = np.array(im.convert('RGB'))
    # print(img[408, 135])
    # pix = img.load
    for i in range(constants.AVAILABLE_TICKETS):
        img = ImageGrab.grab(constants.OUTLINE_BOX[i])
        if (colorExist(img, constants.ORDER_COOKED_RGB)):
            print(str(i) + 'ready')
    # temp = False
    # while (not temp):
    #     if (task_finder.locateTask('cooked_1', constants.COOK_NUM_BOX[0]) or
    #         task_finder.locateTask('cooked_2', constants.COOK_NUM_BOX[0])):
    #         temp = True
    #         print('found')
    #         img = ImageGrab.grab(constants.COOK_NUM_BOX[0])
    #         img.save('temp1.png')
    
           
    