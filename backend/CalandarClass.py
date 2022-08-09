# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:08:01 2022

@author: Preston Waters
"""

#Handles organization of course into valid schedules
class Calandar(object):
    
    #creates numCourses list, each which hold courses
    #taking one course from each list forms a schedule
    def __init__(self, numCourses):
        
        self.bins = []
        self.binTracker = []
        for x in numCourses:
            self.bins.append([])
            self.binTracker.append(0)
     
        
    #adds the items in a list of courses to a bin
    def fillBin(self, binNum, courseList):
        for course in courseList:
            self.bins[binNum].append(course.deepcopy())
       
        
    #removes all items in a bin
    def emptyBin(self, binNum):
        self.bins[binNum].clear()

       
    #Returns a list of the current courses selected
    def getSchedule(self):
        
        #check if schedule is valid 
        valid = True
        for x in range(len(self.binTracker)):
            for y in range(len(self.binTracker)):
                if x != y:
                    valid = self.bins[x][self.binTracker[x]].checkConflict(self.bins[y][self.binTracker[y]])
                if not valid: break
            if not valid: break
        
        #if invalid, find next valid schedule
        if not valid: self.nextCal()
        
        #build and return current schedule
        schedule = []
        for x in range(len(self.binTracker)):
            schedule.append(self.bins[x][self.binTracker[x]])
        
        return schedule

        
        
    #Finds the next valid schedule
    def nextCal(self):
        raise Exception("Needs implementation")
        #catch index out of bounds and return to begining
        #catch empty bins
        
        #what if 0001 and 0010 both work?
        
        
        # https://stackoverflow.com/questions/798854/all-combinations-of-a-list-of-lists
        # https://docs.python.org/2/library/itertools.html#itertools.product
        
        for locked in range(len(self.binTracker)):
            print("temp")
            for x in range(len(self.binTracker)):
    
        
        #each index is locked for 1 run
            #every other combonation with that locked index is checked until
            #a valid schedule is found with a lesser satisfaction value
            
        #the schedule with the highest satisfaction (still lower than previous)
        #is chosen as the next schedule
        
        #with this method, how is "no further schedules" handled?
        
        
        
        
        
    #Finds the next valid schedule
    def prevCal(self):
        raise Exception("Needs implementation")
        #catch index out of bounds and return to end
        #catch empty bins
        
    #An alternative to prevCal that may be better / easier to code
    #A schedule based on an index list is returned
    #This may need some decent error checking
    def getCal(self, indexList):
        raise Exception("Needs implementation")


if __name__ == '__main__': #personal testing code        
        
        raise Exception("No tests here buster")
        
        
        
        
        
        
        
        
        
        
        
        
        
        