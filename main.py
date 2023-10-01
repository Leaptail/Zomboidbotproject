import pyautogui
import time
import random 
import pydirectinput

#Screenshots and so called Memory program
num = 0
#while True:
for x in range(10):
    time.sleep(1)
    img = pyautogui.screenshot("ScreenMemory\Mem%d.png" % num)
    num = num+1
    print("working")