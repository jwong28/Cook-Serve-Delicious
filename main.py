import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract
import time

import constants
import recipes

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def toText(img):
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

    # cv2.imshow("res", res)
    # cv2.waitKey(0)

if __name__ == '__main__': 
    time.sleep(2)
    im = ImageGrab.grab(constants.TICKET_TEXT_BOX)
    im.save('temp.png')
    # text = pytesseract.image_to_string(im, config='--psm 6') 
    img = np.array(im.convert('RGB'))
    text = toText(img)
    recipes.salad(text)
    