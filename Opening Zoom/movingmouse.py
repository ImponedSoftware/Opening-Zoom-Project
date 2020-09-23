import os
import time
import pyautogui

class MyMouse:
    def __init__(self, id, time):
        self.id = id
        self.time = time

    # calls the image detection function within this class with the zoom ID as a parameter
    def runImageDetection(self):
        self.imageDetection(id)

    def openAFile(self, location):
        try:
            os.startfile(location)
        except Exception:
            print('Error opening your file/application.')

    def imageDetection(self, id):
        self.openAFile(r'C:\Users\jonat\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Zoom\Zoom.lnk')
        join_button = 'join.PNG'
        #check = 'check.PNG'

        time.sleep(6)
        print("[movingmouse/imageDetection] 6 second sleep finished")
        os.chdir (r'C:\Users\jonat\OneDrive\Desktop\Opening Zoom (1)\Opening Zoom\Images')
        pyautogui.locateOnScreen(join_button, grayscale=True)        

        print("After locate on screen function")
        pyautogui.click(join_button)
        
        #pyautogui.locateOnScreen(check, confidence = '0.3')
        #x, y = pyautogui.locateCenterOnScreen(check)
        #pyautogui.click(x - 50, y + 10)
        #pyautogui.click(x - 50, y - 51)
        #pyautogui.click(x - 50, y - 317)
        #pyautogui.write(self.id)
        #pyautogui.click(x + 306, y + 119)

        #while(True):
            # find the button continously
            # once the button is found click it

        #while(True):            
            # continously find the next button
            # once the button is found click it

        # once you are in the class, open obs
        # once obs is open, click start recording
        # once it is recording minimize obs
        # set timer for when obs will open again
        # when the time is satisfied, open obs
        # click stop recording
        # create a new folder called zoom lectures and add it to the desktop
        # add your video .mp4 file to your zoom lecture folder



