from tkinter import *
from tkinter import ttk


class SystemViewerView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.controller = None
        self['borderwidth'] = 2
        self['relief'] = 'solid'

    def set_controller(self, controller):
        self.controller = controller
