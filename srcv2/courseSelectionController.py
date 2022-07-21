import re
import tkinter as tk
from tkinter import ttk
from homeview import homeview
from betterqController import betterqController
from courseSelectionview import courseSelectionview
from ApiDatamodel import parseSemesterCourses
import preferenceSelectionController
import ScheduleController
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
    
    def getOtherCoursesCC(self, department):
        x = []
        for key in self.courseDict[department]:
                for y in self.courseDict[department][key]:
                    print(y.data["attribute"])
                    if y.data["attribute"] == "Communitcation Intensive":
                        x.append(y)
        return x
    
    def courseChecked(self, course, state, dept):
        print(course)
        print(state)
        print(dept)
        if(int(state) == 1):
            if course in self.courseDict[dept]:
                self.coursesChecked.append((dept, course))
        elif(int(state) <1):
            self.coursesChecked.remove((dept, course))
        print(self.coursesChecked)
        
    def storeOthercourses(self):
        others = []
        for department in self.courseDict:
            for course in self.courseDict[department]:
                if (department, course) not in self.coursesChecked:
                    for x in self.courseDict[department][course]:
                        others.append(x)
        self.userData.updateOtherCourses(others)
        self.userData.listCopies(self.coursesChecked, self.courseDict, others)
        return others
    
    def updateUserCourses(self):
        for course in self.coursesChecked:
            print(course)
        self.userData.updateuserCourseSelection(self.coursesChecked)
        print(self.userData.getCourseSelection())
        self.storeOthercourses()

        self.switchdisplay()
        
    def switchdisplay(self):
        self.currview.destroy()
        betterq.betterq.switchdisplay(self, ScheduleController.ScheduleController(self.userData))
    def display(self):
        self.currview.display()
   
    