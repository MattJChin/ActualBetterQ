import re
import tkinter as tk
from tkinter import ttk
from homeview import homeview
from betterqController import betterqController
from scheduleview import scheduleview
import betterq

class ScheduleController(betterqController):
    def __init__(self):
        self.currview = scheduleview(self)
        
    #self.title('Tkinter MVC Demo')
        
        # create a model
       
        # create a view and place it on the root window
    def display(self):
        self.currview.display()
   
    