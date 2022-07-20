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
         self.conflits = False
         
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
    
    def checkConflict(self, course2):
        #needs implementation
        return False
        

        
        
if __name__ == '__main__': #personal testing code        
        print("temp")
        
        
        
        
        
        
    
         
         