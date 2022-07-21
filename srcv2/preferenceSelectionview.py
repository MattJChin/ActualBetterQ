import re
import tkinter as tk
from tkinter import ttk
from view import view
class preferenceSelectionview(tk.Tk, view):
    PAD = 10
    BTN_CAPTION = [
        "Schedule",
        "test1",
        "test1",
        "Exit"
    ]
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        
        self._make_mainFrame()
        self._make_title()
      
        
        
    def _make_mainFrame(self):
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)

    """
        Sets view's title.
    """
    def _make_title(self):
        title = ttk.Label(self.mainFrame, text="preference Selection", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)
    def showcommIntesivesdept(self):
        self.courseframe.destroy()
        departments = self.controller.getDepartments()
        departmentframeCi = tk.Frame(self.mainFrame)
        departmentframeCi.pack(fill="x")
        self.departmentframeCi = departmentframeCi
        
        frame_btn = tk.Frame(departmentframeCi)
        frame_btn.pack(fill ="x")
        v = ttk.Scrollbar(departmentframeCi)
        v.pack(side = 'right', fill = 'y')
        for department in departments:
            btn = ttk.Button(frame_btn, text=department, command =lambda txt=department:self.showcommInstensiveclasses(txt))
            btn.pack()
    
    def showcommInstensiveclasses(self, dept):
        self.departmentframeCi.destroy()
        courses = self.controller.getOtherCoursesCC(dept)
        courseframeCi = tk.Frame(self.mainFrame)
        courseframeCi.pack(fill="x")
        self.courseframeCi = courseframeCi
        
        frame_checkbtn = tk.Frame(courseframeCi)
        
        frame_checkbtn.pack()
        
        varlist = []
        for index, course in enumerate(courses):
            intvar = 0
            varlist.append(tk.StringVar())
            checkbtn = ttk.Checkbutton(frame_checkbtn, text=course, variable= varlist[index], onvalue = 1, offvalue =0, command =lambda state=index, txt=course:self.controller.courseChecked(txt, varlist[state].get()))
            checkbtn.pack()
        
        btn = ttk.Button(frame_checkbtn, text="submit", command =lambda: self.controller.updateUserCourses())
        btn.pack()
       
        
    def display(self):
        self.controller.updateUserCourses()
        self.mainloop()
        # set the controller to view
        # set the controller to view
    
