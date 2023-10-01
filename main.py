import pyautogui
import time
import random 
import pydirectinput
import cv2

#Screenshots and so called Memory program
num = 0
#while True:
"""for x in range(100):
    time.sleep(1)
    img = pyautogui.screenshot("ScreenMemory\Mem%d.png" % num)
    num = num+1
    print("working")"""

#lets start by making it run away from zombies
"""for abc in range(1,6):
    Tradefrom = pyautogui.locateCenterOnScreen("BuiltMem\Mem%d.png" % abc, confidence=0.55)
    if Tradefrom == None:
        print("notfound")
        continue
    else:
        x, y = Tradefrom
        print("found")"""
for abc in range(1,10):
    x,y =pyautogui.size()
    print(x,y)
