import re
import tkinter as tk
from tkinter import ttk
from homeview import homeview
from betterqController import betterqController
from scheduleview import scheduleview
import betterq

class ScheduleController(betterqController):
    def __init__(self, userData):
        self.currview = scheduleview(self)
        self.userData = userData
        
    #self.title('Tkinter MVC Demo')
    
    def generateSchedule(self):
        print("-------------------------------------------------------------------------------------")
        self.coursesCal = self.userData.getOthercoursedict()
        indexes = []
        for x in self.coursesCal:
            print(x)
            indexes.append(0)
        
    #This compares each course being looked at to the ones after it
    #if they match, we move to the next course in the second sublist
    #until they dont. This way, we have a unique course selected from
    #each sublist.
        i = 0
        for x in indexes:
            base = self.coursesCal[i][x].data["title"]
            j = 0
            for y in range(len(indexes)):
                if( j > i ):
                    while base == self.coursesCal[j][indexes[y]].data["title"]:
                        indexes[y]+=1
                j+=1
            i+=1
            
            
        #print the selected courses 
        i = 0
        for courses in self.coursesCal:
            print(courses[indexes[i]].data["title"])
            i+=1
        
        # create a model
        print("--------------------------------------------------------------------------------")
        # create a view and place it on the root window
    def display(self):
        self.currview.display()
   
    