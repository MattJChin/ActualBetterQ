
class userData(object):
    
    def __init__(self):
        self.userCourseSelection =[]
        
    def updateuserCourseSelection(self, courses):
       
       for course in courses:
        print(course)
        self.userCourseSelection.append(course)

    def getCourseSelection(self):
        return self.userCourseSelection
        

        
        
        
        
        
    
         
         