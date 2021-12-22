from tkinter import *
from tkinter import ttk, StringVar


class MainDisplayView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.winfo_parent()
        self.parent.title('Feet to Meters')

        mainframe = ttk.Frame(self.parent, padding='3 3 12 12')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)

        mainframe.columnconfigure(1, weight=1, minsize=50)
        mainframe.columnconfigure(2, weight=1, minsize=50)
        mainframe.columnconfigure(3, weight=1, minsize=50)
        mainframe.rowconfigure(1, weight=1, minsize=50)
        mainframe.rowconfigure(2, weight=1, minsize=50)
        mainframe.rowconfigure(3, weight=1, minsize=50)

        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))

        self.meters = StringVar()
        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(mainframe, text='Calculate', command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text='feet').grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text='is equivalent to').grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text='meters').grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        self.parent.bind('<Return>', self.calculate)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def calculate(self, *args):
        if self.controller:
            self.controller.calculate(*args)