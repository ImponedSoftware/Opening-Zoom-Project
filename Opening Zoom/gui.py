from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import pyautogui
import classroom
import movingmouse

class GUI:
    # constructor
    def __init__(self, name, master, count):
        self.name = name
        self.master = master
        self.count = count
        self.save_data = []
        master.title(name)
    # methods

    def hello(self):
        print("Hello")

    def createMenu(self):
        # creates menu object
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # creates a label with text to display on your window
        Label(self.master,text="                                                                                                                                                                                                                   ").grid(row=0,column=0)
        Label(self.master, text = 'Smartass', font =( 
        'Verdana', 25)).grid(row=0,column=20) 

        # creates image for your button
        global icon

        # photo button missing
        icon = PhotoImage(file=r"C:\Users\jonat\OneDrive\Desktop\Opening Zoom (1)\Opening Zoom\Images\cButton.png")

        # creates button with the same dimensions as your image
        Button(self.master, image=icon, compound=CENTER, command = self.promptButton).grid(row=1,column=20)
        
    def myCheckBox(self, myclass, myrow):
        # creates a check box at grid location on your window
        var1 = IntVar()
        Checkbutton(self.master, text=myclass, variable=var1).grid(row=myrow, sticky=W)    
        

    def promptButton(self):
        self.count += 1
        classname = pyautogui.prompt('- Type in your class name -')
        ID = pyautogui.prompt('- Type in your zoom ID -')
        m = movingmouse.MyMouse(ID, 2)

        Class = classroom.myClass(classname, 5, 30, "am", ID)
        self.save_data.append(Class)

        Label(self.master, text=classname, font=('Verdana',15)).grid(row=self.count+2,column=20)
        Button(self.master, text="Join", command=m.runImageDetection).grid(row=self.count+2,column=21) 

    def saveData(self):
        # for each class in my list, save to text file including all fields
        save_text_file = open("save.txt", "w")

        # CHECK THIS
        for i in range(1, len(self.save_data)):
            print(i)

        print("After saved data")


    def readData(self):
        print("qd")

        # for every line in my text file read class and store into list

    #def changeZoomID(self, my_class, new_zoom_id):
        # change your zoom id for that specific class