# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:08:01 2022

@author: Preston Waters
"""

#Handles the full data management of all courses
class Calandar(object):
    
    #takes as input user prefrences
    #forms internal data structure similar to listCopies(), i.e.,
    #a list where each entry is a list of possible courses for that "slot"
    #For example, if you have to take Robotics I and Writing I
    #The first list is all Robotics I sections,
    #The second list is all Writing I sections
    #If you need a 4000 level BIOL course, the third list would
    #be all of the 4000 level BIOL courses
    #the remaining lists will be duplicate lists of all other courses
    #these will be modified and sorted based on user input
    def __init__(self):
        print('temp')
        
        """
        okay so, this class is going to handle all my shitty data management
        the problem is most of it is going to depend on how this class needs
        to talk to the front end.
        
        it will take over mose of the duties from listify and listCopies in main
        
        see the "boxes" analogy that will be better coded haha
        
        -note: make harder specs like com intenive biol its own box
        
        """
    #Sends a group of courses, 
    #which ever the current index from each box is to the front end
    def generate():
        raise Exception("Needs implementation")
        
    #move an index further to find the next most valuable schedule
    #checking for conflicts
    def nextCal():
        raise Exception("Needs implementation")
        

if __name__ == '__main__': #personal testing code        
        
        raise Exception("No tests here buster")
        
        
        
        
        
        
        
        
        
        
        
        
        
        