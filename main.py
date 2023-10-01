import pyautogui
import time
import random 
import pydirectinput
import cv2

#screen dimensions 2560 by 1440, midpoints 1281,721
#Screenshots and so called Memory program
num = 0
#while True:
"""for x in range(100):
    time.sleep(1)
    img = pyautogui.screenshot("ScreenMemory\Mem%d.png" % num)
    num = num+1
    print("working")"""

#lets start by making it run away from zombies
while True:
    for abc in range(1,26):
        Tradefrom = pyautogui.locateCenterOnScreen("BuiltMem\Mem%d.png" % abc, grayscale = True, confidence=0.6)
        if Tradefrom == None:
            print("notfound")
            pydirectinput.keyUp('d')
            pydirectinput.keyUp('a')
            pydirectinput.keyUp('s')
            pydirectinput.keyUp('w')
            continue
        else:
            x, y = Tradefrom
            print("found")
            if x-1281>=0:
                pydirectinput.keyDown('a')
                pydirectinput.keyUp('d')
            elif x-1281<0:
                pydirectinput.keyDown('d')
                pydirectinput.keyUp('a')
            if y-721>=0:
                pydirectinput.keyDown('w')
                pydirectinput.keyUp('s')
            elif y-721<0:
                pydirectinput.keyDown('s')
                pydirectinput.keyUp('w')
    



