from tkinter import *
from tkinter import ttk
from system_viewer.views.system_viewer_view import SystemViewerView


class GraphView(SystemViewerView):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text='CECI EST LE GRAPHVIEW').grid(column=0, row=0, sticky=(N, W, E, S))

