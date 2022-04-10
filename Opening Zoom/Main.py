import sys
print("YOUR PATH: ", sys.path)

import os
import time
import pyautogui
import datetime
import movingmouse
import gui
import classroom
from tkinter import *

# selenium module for pip3


window = Tk()
# arg1(name of project), arg2(Tkinter object), arg3(index pos)
interface = gui.GUI("Zoom Join Automation Software", window, 0)
interface.readData()
interface.createMenu()
window.mainloop()
interface.saveData()


#def runAtThisTime(m, d, h, m, s, pa):
 #   currentDT = datetime.datetime.now()

 #   if(currentDT.month == m and currentDT.day == d):
  #      if(currentDT.hour == h and currentDT.minute == m and currentDT.second == s):
   #         print("Do this...")

# debugging


def mouseLocation():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4) 
            pixelColor = pyautogui.screenshot().getpixel((x, y))
            positionStr += " RGB: (" + str(pixelColor[0]).rjust(3)
            positionStr += ", " + str(pixelColor[1]).rjust(3)
            positionStr += ", " + str(pixelColor[2]).rjust(3) + ")"           
            print(positionStr)
    except KeyboardInterrupt:
        print('\nDone.')

#mouseLocation()



