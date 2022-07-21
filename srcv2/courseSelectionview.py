import re
import tkinter as tk
from tkinter import ttk
from view import view
class courseSelectionview(tk.Tk, view):
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
        self.showdepartments()
        
    def _make_mainFrame(self):
        self.mainFrame = ttk.Frame(self)
        v = ttk.Scrollbar(self.mainFrame, orient = "vertical")
        v.pack(side = "right", fill = "y")
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)
       
        
        
    def test(self):
        print("testfail")
        
    
    
    def _make_title(self):
        title = ttk.Label(self.mainFrame, text="course Selection", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)
        
        
    def showdepartments(self):
        departments = self.controller.getDepartments()
        departmentframe = tk.Frame(self.mainFrame)
        departmentframe.pack(fill="x")
        self.departmentframe = departmentframe
        
        frame_btn = tk.Frame(departmentframe)
        frame_btn.pack(fill ="x")
        v = ttk.Scrollbar(departmentframe)
        v.pack(side = 'right', fill = 'y')
        for department in departments:
            btn = ttk.Button(frame_btn, text=department, command =lambda txt=department:self.showclasses(txt))
            btn.pack()
        # Show header
        
    def showclasses(self, dept):
        self.departmentframe.destroy()
        courses = self.controller.getCourses(dept)
        courseframe = tk.Frame(self.mainFrame)
        courseframe.pack(fill="x")
        self.courseframe = courseframe
        
        frame_checkbtn = tk.Frame(courseframe)
        
        frame_checkbtn.pack()
        
        varlist = []
        for index, course in enumerate(courses):
            intvar = 0
            varlist.append(tk.StringVar())
            checkbtn = ttk.Checkbutton(frame_checkbtn, text=course, variable= varlist[index], onvalue = 1, offvalue =0, command =lambda state=index, txt=course:self.controller.courseChecked(txt, varlist[state].get()))
            checkbtn.pack()
        
        btn = ttk.Button(frame_checkbtn, text="submit", command =lambda: self.controller.updateUserCourses())
        btn.pack()
       
        # Show header
    
        
    def display(self):
        self.mainloop()
        # set the controller to view
        # set the controller to view
    
