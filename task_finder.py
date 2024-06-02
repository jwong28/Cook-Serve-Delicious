import pyautogui

def locateTask(name, reg):
    fileName = 'data/' + name + '.png'
    try:
        loc = pyautogui.locateOnScreen(fileName, region=reg, confidence=0.80)
        print(loc)
        return True
    except:
        return False

