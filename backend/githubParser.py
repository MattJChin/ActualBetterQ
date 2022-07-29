# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 12:09:06 2022

@author: Preston Waters
"""
#If betterQ were ever to be implemented into QuACS,
#This code would be redundant since they already parse from SIS
#I just don't understand the formatting they use.
#They seems to have very robust scrapers though for all kinds of things
#that we don't know how to get. It may be beneficial to talk to Ben
#Sherman about collaberation... 7/4/2022

from urllib.request import urlopen
import json
import courseClass

import requests
from bs4 import BeautifulSoup

#Finds the newest version of the course database from QuACS github
#This was we don't have to download the whole repository
def findUrl():

    url = 'https://github.com/quacs/quacs-data/tree/master/semester_data' 
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    first = ''
    second = ''
    #goes through every link on the page to find newest data
    for link in soup.find_all('a'):
        second = first
        first = link.get('href')
        
        #when first is https://github.com, that means the previous link was the last file link
        #i.e., the newest data
        if(first == 'https://github.com'):
            start = 'https://raw.githubusercontent.com/quacs/quacs-data/master/semester_data/'
            end = '/courses.json'
            return(start + second[44::] + end)
            
    raise Exception("URL not found.")


#builds a dictionary of dictionaries fo lists
#the first keys are 4 letter course codes
#the inner keys are the names of the course
#and the inner values are lists of courseClass instances
def parseSemesterCourses():
    
    #find the url
    url = findUrl() 
    
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON data from the response
    data = json.loads(response.read())
    
    #note: This assumes the data is always formatted correctly
    #and is complete. I can't see why it wouldn't be, but error
    #proofing may be in order.
    
    departmentDict = {}
    
    #sort data into courseClass instances
    for departments in data:
        for course in departments["courses"]:
            for section in course["sections"]:
                                
                #create department key (eg "BIOL") if needed
                if departmentDict.get(section["subj"]) is None:
                    departmentDict[section["subj"]] = {}
                  
                #create list of this course in that department (eg. sections of biology 101)
                if departmentDict[section["subj"]].get(section["title"]) is None:
                    departmentDict[section["subj"]][section["title"]] = []
                
                #add this instance (section) of the course to the list
                departmentDict[section["subj"]][section["title"]].append(courseClass.Course(section))
                    
                
                #note: how are double listings handled, do I even care?
                #ie something listed as a phylosophy and biology course (bioethics)
                #I don't think I should care that much, but might be nice
                #for double relevancy...
                
    
    return departmentDict


    


if __name__ == '__main__': #personal testing code
    
    departmentDict = parseSemesterCourses()
    
    #testing time conflict code with some random course
    compareTo = departmentDict["CSCI"]["Robotics I"][0]
    
    for department in departmentDict:
        for course in departmentDict[department]:
    
            compareTo.checkConflict(departmentDict[department][course][0])

    
    

    












    