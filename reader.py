import pyautogui
from PIL import ImageGrab, Image
import cv2
import numpy as np
import pytesseract
import time

from constants import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def locateTask(name, reg):
    fileName = 'data/' + name + '.png'
    try:
        loc = pyautogui.locateOnScreen(fileName, region=reg, confidence=0.60)
        # print(loc)
        return True
    except:
        return False

def locateFood(name):
    return locateTask(name, FOOD_BOX)

def getTicketText():
    im = ImageGrab.grab(TICKET_TEXT_BOX)
    img = np.array(im.convert('RGB'))
    return imageToText(img)

def getTicketTitle():
    im = ImageGrab.grab(TICKET_TITLE_BOX)
    img = np.array(im.convert('RGB'))
    return imageToText(img)

def getButtonText():
    im = ImageGrab.grab(BUTTON_BOX)
    img = np.array(im.convert('RGB'))
    return imageToText(img)


def imageToText(img):
    # Convert to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv = resize_img(hsv, 300)
    # cv2.imshow("img", hsv)
    # cv2.waitKey(0)

    # Get the binary mask
    msk = cv2.inRange(hsv, np.array([0, 0, 0]), np.array([179, 255, 154]))

    # Extract
    krn = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
    dlt = cv2.dilate    (msk, krn, iterations=5)
    res = 255 - cv2.bitwise_and(dlt, msk)

    # OCR
    txt = pytesseract.image_to_string(res, config="--psm 6")
    # print('hello ' + txt)
    return txt.lower().strip()

def resize_img(img, scale):

    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)

    dsize = (width, height)
    
    return cv2.resize(img, dsize=dsize)

def colorExist(img, colors):
    existing = []
    width, height = img.size
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            if ((r, g, b) in colors):
                return True
    #         if ((r, g, b) not in existing):
    #             existing.append((r, g, b))
    # print(existing)
    return False

def checkIfLit(img):
    return colorExist(img, [AVAIALABLE_ORDER_RGB])

def checkIfCooked(img):
    return colorExist(img, ORDER_COOKED_RGB)

def checkIfPhase2(img):
    return colorExist(img, ORDER_PHASE2_RGB)
