import re
import tkinter as tk
from tkinter import ttk
from view import view
class homeview(tk.Tk, view):
    PAD = 10
    BTN_CAPTION = [
        "Schedule view",
        "Course Selection view",
        "Preference Selection view",
        "Exit"
    ]
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        
      

        # create a model
       
    
        # create a view and place it on the root self.root
    
        self._make_mainFrame()
        self._make_title()
        self._make_options()
        
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        Creates view's frame.
    """
    def _make_mainFrame(self):
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)

    """
        Sets view's title.
    """
    def _make_title(self):
        title = ttk.Label(self.mainFrame, text="BetterQ home page", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)
        
    """
        Creates view's options.
    """
    def _make_options(self):
        frame_btn = ttk.Frame(self.mainFrame)
        frame_btn.pack(fill="x")
        
        for caption in self.BTN_CAPTION:
            print(caption)
            if caption == "Exit":
                btn = ttk.Button(frame_btn, text=caption, command =self.destroy)
            else:
                btn = ttk.Button(frame_btn, text=caption, command=lambda txt=caption: self.switchdisplay(txt))
            
            btn.pack(fill="x")
    def switchdisplay(self, caption):
        self.controller.btnClicked(caption)
    def display(self):
        self.mainloop()
        # set the controller to view
        # set the controller to view

    
