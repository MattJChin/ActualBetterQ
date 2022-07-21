import re
import tkinter as tk
from tkinter import ttk
from homeview import homeview 
from betterqController import betterqController
import courseSelectionController
import preferenceSelectionController
import ScheduleController

import userDatamodel
import betterq

class homeController(betterqController):
    def __init__(self):
        self.currview = homeview(self)
        self.userData = userDatamodel.userData()
    #self.title('Tkinter MVC Demo')
    
        # create a model
    def btnClicked(self, caption):
        print(caption)
        self.currview.destroy()
        if caption == "Course Selection view":
            print("test2")
            betterq.betterq.switchdisplay(self, courseSelectionController.courseSelectionController(self.userData))
            
        elif caption == "Preference Selection view":
            print("test1")
            betterq.betterq.switchdisplay(self, preferenceSelectionController.preferenceSelectionController())
        elif caption == "Schedule view":
            print("test3")
            betterq.betterq.switchdisplay(self, ScheduleController.ScheduleController())
        
        # create a view and place it on the root window
    def display(self):
        self.currview.display()
        

   
    