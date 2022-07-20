import re
import tkinter as tk
from tkinter import ttk
import abc

#abstract view class
class view(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display(self):
        return
    


