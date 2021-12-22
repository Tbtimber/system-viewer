from tkinter import *
from system_viewer.controllers.main_display_controller import MainDisplayController
from system_viewer.views.main_display_view import MainDisplayView

if __name__ == '__main__':
    root = Tk()
    root.option_add('*tearOff', FALSE)
    view = MainDisplayView(root)
    controller = MainDisplayController(None, view)
    view.set_controller(controller)
    root.mainloop()
