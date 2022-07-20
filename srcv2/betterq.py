import re
import tkinter as tk
from tkinter import ttk
from homeController import homeController

from view import view
from betterqController import betterqController

class betterq():
    def __init__(self):
       self.controller = homeController()
       self.controller.display()
    #self.title('Tkinter MVC Demo')
    
    def switchdisplay(self, newDisplay):
        self.controller= newDisplay
        print("test")
        self.controller.display()
           
        
        # create a model
       

     
   
   

 
    


