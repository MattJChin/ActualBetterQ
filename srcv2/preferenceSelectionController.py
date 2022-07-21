import re
import tkinter as tk
from tkinter import ttk
from homeview import homeview
from betterqController import betterqController
from preferenceSelectionview import preferenceSelectionview
from userDatamodel import userData
import betterq

class preferenceSelectionController(betterqController):
    def __init__(self, userdata):
        self.currview = preferenceSelectionview(self)
        self.userData = userdata
    #self.title('Tkinter MVC Demo')
    def updateUserCourses(self):
        print(self.userData.getCourseSelection())
       
        # create a view and place it on the root window
    def display(self):
        self.currview.display()
   
    