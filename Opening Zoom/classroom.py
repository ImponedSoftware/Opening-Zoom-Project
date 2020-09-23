import os
import time
import pyautogui

class myClass:
    def __init__(self, className, hour, minute, ampm, zoomID):
        self.className = className
        self.hour = hour
        self.minute = minute
        self.ampm = ampm
        self.zoomID = zoomID
        
    
    def setTime(self, h, m, ap):
        self.hour = h
        self.minute = m
        self.ap = ap

    def setZoomID(self, id):
        self.zoomID = id

