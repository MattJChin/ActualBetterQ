import re
import tkinter as tk
from tkinter import ttk
from homeview import homeview
from betterqController import betterqController
from preferenceSelectionview import preferenceSelectionview
import betterq

class preferenceSelectionController(betterqController):
    def __init__(self):
        self.currview = preferenceSelectionview(self)
        
    #self.title('Tkinter MVC Demo')
        
        # create a model
       
        # create a view and place it on the root window
    def display(self):
        self.currview.display()
   
    