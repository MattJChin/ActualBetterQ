# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 19:14:26 2022

@author: Preston Waters
"""
from githubParser import parseSemesterCourses
 
#prompt the user to select courses they are required to take
def selectReqs(departmentDict):
    
    requiredKeys = []
    
    print("Please select required courses")
    print("Input 4 character code for department (case sensitive)")
    
    for key, value in departmentDict.items() :
        print(key)
    
    dept = input("Input subject code or type NEXT to continue: ")
    
    while(dept != "NEXT"):
        if dept in departmentDict:
            for key, value in departmentDict[dept].items() :
                print(key)
            select = input("Please type the name of a course, or type BACK to go back: ")
            while(select != "BACK"):
                if select in departmentDict[dept]:
                    print(select + " selected.")
                    requiredKeys.append((dept, select))
                else:
                    print("Invalid input.")
                select = input("Please type the name of a course, or type BACK to go back: ")
            for key, value in departmentDict.items() :
                print(key)
        elif(dept == "NEXT"):
            print("Moving to prefrence selection")
        else:
            print("Invalid input.")
            
        dept = input("Input subject code or type NEXT to continue: ")
    
    #returning a list of touples eg ("CSCI", "Computer Science I")
    #this is the key pair for the list of comp sci 1 courseClasses
    return requiredKeys
    
#reorganize course data into a list for prefrence & calander management
#list will ommit required courses
def listify(departmentDict, requiredKeys):
    
    otherCourses = []
    #for key in dict
    for department in departmentDict:
        for course in departmentDict[department]:
            if (department, course) not in requiredKeys:
                for x in departmentDict[department][course]:
                    otherCourses.append(x)
    
    return otherCourses
 
#create a list where each entry is a list of possible courses
#the first entires will be lists of sections of required courses
#I.e., first list would be all sections of Robotics I
#the remaining lists will be duplicate lists of all other courses
#these will be modified and sorted later based on user input
def listCopies(requiredKeys, departmentDict, courseList): 
    
    courses = []
    
    print("Your required courses are:")
    for key in requiredKeys:
        print(key[1])
        courses.append(departmentDict[key[0]][key[1]])
        
        
    #note: this will break with bad user input
    num = int(input("How many courses would you like to take? "))
    for x in range(num):
        courses.append(courseList.copy())
    
    return courses
    
#evaluates courses based on user prefrences
#this may leave required coursed rated very lowly
#I don't care though since their in their own list theyre required
#If I change the alogrithm that may have to change tho
#note: this currently assumes user inputs perfectly
def evaluate(courseList):
    
    user = input("Do you need a communication intensive course? Y/N: ")
    if user == "Y":
        print("ADMN USAF ARCH ARTS ASTR BCBP BIOL BMED BUSN CHME CHEM")
        print("CIVL COGS COMM CSCI ENGR ERTH ECON ECSE ESCI ENVE GSAS")
        print("ISYE ITWS IENV IHSS ISCI LANG LGHT LITR MGMT MTLE MATP")
        print("MATH MANE USAR USNA PHIL PHYS PSYC STSO WRIT")
        user = input("Which department do you need that in?: ")
        for group in courseList:
            for course in group:
                if course.data["attribute"] == "Communication Intensive" and course.data["subj"] == user:
                    course.relevancy+=100
        
    user = input("Do you need a 4000 level course? Y/N: ")
    if user == "Y":
        print("ADMN USAF ARCH ARTS ASTR BCBP BIOL BMED BUSN CHME CHEM")
        print("CIVL COGS COMM CSCI ENGR ERTH ECON ECSE ESCI ENVE GSAS")
        print("ISYE ITWS IENV IHSS ISCI LANG LGHT LITR MGMT MTLE MATP")
        print("MATH MANE USAR USNA PHIL PHYS PSYC STSO WRIT")
        user = input("Which department do you need that in?: ")
        for group in courseList:
            for course in group:
                if 5000 > course.data["crse"] >= 4000 and course.data["subj"] == user:
                    course.relevancy+=100
        
    user = input("Would you like to choose an earliest time to start? Y/N: ")
    if user == "Y":
        user = input("Please input an earliest time in military format, eg 1:30 is 1330: ")
        for group in courseList:
            for course in group:
                for time in course.data["timeslots"]:
                    if time["timeStart"] < int(user):
                        course.relevancy-=25
                    else:
                        course.relevancy+=25
        
          
        
    user = input("Would you like to select departments of interest? Y/N: ")
    if user == "Y":
        print("Enter as many of the following as you would like or type DONE to finish.")
        print("ADMN USAF ARCH ARTS ASTR BCBP BIOL BMED BUSN CHME CHEM")
        print("CIVL COGS COMM CSCI ENGR ERTH ECON ECSE ESCI ENVE GSAS")
        print("ISYE ITWS IENV IHSS ISCI LANG LGHT LITR MGMT MTLE MATP")
        print("MATH MANE USAR USNA PHIL PHYS PSYC STSO WRIT")
        
        user = input("Input department code or BACK:")
        
        #this assumes the user never gives bad input or the same input
        #more than once
        while user != "NEXT":
            for group in courseList:
                for course in group:
                    if course.data["subj"] == user:
                        course.relevancy+=25
                    else:
                        course.relevancy-=25
            user = input("Input department code or NEXT:")
                    
    return

if __name__ == '__main__':
    
    departmentDict = parseSemesterCourses()
    requiredKeys = selectReqs(departmentDict)
    courseList = listify(departmentDict, requiredKeys)
    
    
    #formats courseList better to make calanders later
    coursesCal = listCopies(requiredKeys, departmentDict, courseList)
  

    #evaluate courses by user prefrence
    evaluate(coursesCal)
    
    #sort each list from most to least relevant
    for courses in coursesCal: 
        courses.sort(key=lambda x: x.relevancy, reverse=True)  
     
    #coursesCal is a list of lists,
    #courseCal has as many sub lists as the user wants course
    #i.e. 4 sublists means they are taking 4 courses
    #each of these sublists holds possible courses to fit in that slot
    
    #This tracks which course is being looked at in each sublist
    indexes = []
    for x in coursesCal:
        indexes.append(0)
        
    #This compares each course being looked at to the ones after it
    #if they match, we move to the next course in the second sublist
    #until they dont. This way, we have a unique course selected from
    #each sublist.
    i = 0
    for x in indexes:
        base = coursesCal[i][x].data["title"]
        j = 0
        for y in range(len(indexes)):
            if( j > i ):
                while base == coursesCal[j][indexes[y]].data["title"]:
                    indexes[y]+=1
            j+=1
        i+=1
        
        
    #print the selected courses 
    i = 0
    for courses in coursesCal:
        print(courses[indexes[i]].data["title"])
        i+=1
    
    
    #note: Program needs time conflict avoidance implementation
    
    #note: Program rates things very basically, so if you say you need
    #a 4000 level art course, it increases the raiting of all 4000 level
    #arts courses, leading your schedule to likely contain two of them.
    #This is another conflict that needs to be handled.
    #It may be a good idea to redesign algorithm from the ground up.
    #The box slots method is a good start, I just think filling in
    #the free courses with every possible course may not be the best
    #way to go.
    
    
        
    