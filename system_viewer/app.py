from tkinter import *
from tkinter import ttk

from system_viewer.controllers.main_display_controller import MainDisplayController
from system_viewer.views.main_display_view import MainDisplayView


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('System viewer')
        self.minsize(500, 350)
        model = None
        self.main_view = MainDisplayView(self)
        controller = MainDisplayController(model, self.main_view)

        self.main_view.set_controller(controller)

        self.main_view.grid(column=0, row=0, sticky=(N, E, S, W))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
