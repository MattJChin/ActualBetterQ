import abc



class betterqController(metaclass=abc.ABCMeta): 
    @abc.abstractmethod
    def display(self):
       return
   
    def switchdisplay(self, newDisplay):
        self.currview= newDisplay
        self.currview.display()
    