
class userData(object):
    
    def __init__(self):
        self.userCourseSelection =[]
        self.otherCourses = []
        self.othcoursedict= []
    def updateuserCourseSelection(self, courses):
       for course in courses:
        print(course)
        self.userCourseSelection.append(course)
    
    def updateOtherCourses(self, courses):
        self.othcoursedict = courses
        for course in courses:
            print(course)
            self.otherCourses.append(course)

    def getCourseSelection(self):
        return self.userCourseSelection
    
    def listCopies(self, requiredKeys, departmentDict, courseList): #should go into course model class
        courses = []
        for key in requiredKeys:
            print(key[1])
            courses.append(departmentDict[key[0]][key[1]])
            
            
        #note: this will break with bad user input
        num = 6
        for x in range(num):
            courses.append(courseList.copy())
        self.othcoursedict = courses
        return courses
    def getOthercoursedict(self):
        self.evaluate()
        return self.othcoursedict
    
    def evaluate(self):   #this should be split between preferenceselection view and prefrence selection controller    

            
        user = "Y"
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
                for group in self.othcoursedict:
                    print(group)
                    for course in group:
                        print(course)
                        if course.data["subj"] == user:
                            course.relevancy+=25
                        else:
                            course.relevancy-=25
                user = input("Input department code or NEXT:")
                        
        return
    
    
    
    
  
    
        

        
        
        
        
        
    
         
         