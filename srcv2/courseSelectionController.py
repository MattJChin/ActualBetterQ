import re
import tkinter as tk
from tkinter import ttk
from homeview import homeview
from betterqController import betterqController
from courseSelectionview import courseSelectionview
from ApiDatamodel import parseSemesterCourses
import preferenceSelectionController
import betterq

class courseSelectionController(betterqController):
    def __init__(self, usermodel):
        self.currview = courseSelectionview(self)
        self.userData = usermodel
    
    
    #add functions from mainv1(ex. selectReqs(), )
    def getCourseData(self):
        self.courseDict = parseSemesterCourses()
        self.coursesChecked = []
    def getDepartments(self):
        
        self.getCourseData()
        x =[]
        for key, value in self.courseDict.items():
            x.append(key)
        return x
    
    def getCourses(self, department):
        x = []
        for key, value in self.courseDict[department].items() :
            x.append(key)
        return x
    
    def courseChecked(self, course, state):
        print(course)
        print(state)
        if(int(state) == 1):
            self.coursesChecked.append(course)
        elif(int(state) <1):
            self.coursesChecked.remove(course)
        print(self.coursesChecked)
    def getCheckedCourses(self):
    
        return self.coursesChecked
    
    def updateUserCourses(self):
        for course in self.coursesChecked:
            print(course)
        self.userData.updateuserCourseSelection(self.coursesChecked)
        print(self.userData.getCourseSelection())
        self.switchdisplay()
    def switchdisplay(self):
        self.currview.destroy()
        betterq.betterq.switchdisplay(self, preferenceSelectionController.preferenceSelectionController(self.userData))
    def display(self):
        self.currview.display()
   
    