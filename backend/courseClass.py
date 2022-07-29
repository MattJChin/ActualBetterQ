# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 23:15:58 2022

@author: Preston Waters
"""

#need more robust class design
#create a test version of the file for parser

#holds the data for a single section of a given course
class Course(object):
    
    def __init__(self, dataIn):
         self.data = dataIn
         self.relevancy = 0
         self.timeBlock = []
         
         #sample data
         """
        "act": 10,
        "attribute": "Introductory Level Course",
        "cap": 60,
        "credMax": 4.0,
        "credMin": 4.0,
        "crn": 56913,
        "crse": 1100,
        "rem": 50,
        "sec": "04",
        "subj": "CHEM",
        "timeslots": [
          {
            "dateEnd": "12/20",
            "dateStart": "08/29",
            "days": [
              "T",
              "F"
            ],
            "instructor": "Steven A. Tysoe, Alexander C. Ma",
            "location": "Darrin Communications Center 308",
            "timeEnd": 1350,
            "timeStart": 1200
          },
          {
            "dateEnd": "12/20",
            "dateStart": "08/29",
            "days": [
              "T"
            ],
            "instructor": "Kathleen Lillian Morrissey",
            "location": "Walker Laboratory 5113",
            "timeEnd": 950,
            "timeStart": 800
          },
          {
            "dateEnd": "12/20",
            "dateStart": "08/29",
            "days": [
              "T"
            ],
            "instructor": "TBA",
            "location": "TBA",
            "timeEnd": 1050,
            "timeStart": 1000
          },
          {
            "dateEnd": "12/20",
            "dateStart": "08/29",
            "days": [
              "W"
            ],
            "instructor": "TBA",
            "location": "Darrin Communications Center 308",
            "timeEnd": 850,
            "timeStart": 800
          }
        ],
        "title": "Chemistry I"
        """
         
    def adjRelevancy(self, change):
        self.relevancy = self.relevancy + change
    
    
    #return true if the courses overlap at all
    #otherwise return false
    def checkConflict(self, course2):
        
        #build a list of touples representing
        #the start and end times of each time block
        #since comparisons will likely have to be made again later
        #this info is saved for reuse.
        if not bool(self.timeBlock):
            for time in self.data["timeslots"]:
                timeStart = time["timeStart"]
                timeEnd = time["timeEnd"]
                add = 0
                for day in time["days"]:
                    if(day == 'M'): add = 2400
                    if(day == 'T'): add = 4800
                    if(day == 'W'): add = 7200
                    if(day == 'R'): add = 9600
                    if(day == 'F'): add = 12000
                    
                    #add and put in list
                    block = (timeStart+add, timeEnd+add)
                    self.timeBlock.append(block)
        
        #Load time block of other course if needed
        if not bool(course2.timeBlock):
            for time in course2.data["timeslots"]:
                timeStart = time["timeStart"]
                timeEnd = time["timeEnd"]
                add = 0
                for day in time["days"]:
                    if(day == 'M'): add = 2400
                    if(day == 'T'): add = 4800
                    if(day == 'W'): add = 7200
                    if(day == 'R'): add = 9600
                    if(day == 'F'): add = 12000
                    
                    #add and put in list
                    block = (timeStart+add, timeEnd+add)
                    course2.timeBlock.append(block)
                
        for x in self.timeBlock:
            for y in course2.timeBlock:
                if(y[0] <= x[0] and y[1] >= x[0]):
                    print("----------------COURSE 1----------------")
                    print(self.data["title"])
                    print(self.data["timeslots"])
                    print("----------------COURSE 2----------------")
                    print(course2.data["title"])
                    print(course2.data["timeslots"])
                    return True
                if(y[0] <= x[1] and y[1] >= x[1]):
                    print("----------------COURSE 1----------------")
                    print(self.data["title"])
                    print(self.data["timeslots"])
                    print("----------------COURSE 2----------------")
                    print(course2.data["title"])
                    print(course2.data["timeslots"])
                    return True
            
        return False

        
        
if __name__ == '__main__': #personal testing code        
        print("temp")

        
    
         
         