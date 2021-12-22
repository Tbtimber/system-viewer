from tkinter import *

from system_viewer.views.graph_view import GraphView
from system_viewer.views.panel_view import PanelView
from system_viewer.views.system_viewer_view import SystemViewerView


class MainDisplayView(SystemViewerView):
    def __init__(self, parent):
        super().__init__(parent)

        # Initialize graph view
        self.graph_view = GraphView(self)
        self.graph_view.grid(column=1, row=1, columnspan=3, sticky=(N, W, E, S))
        self.graph_view.bind('<ButtonPress-1>', self.do_background_task)

        # Initialize left panel
        self.left_panel_view = PanelView(self)
        self.left_panel_view.grid(column=1, row=1, columnspan=1, sticky=(N, S, W))

        # Initialize right panel
        self.right_panel_view = PanelView(self)
        self.right_panel_view.grid(column=3, row=1, columnspan=1, sticky=(N, S, E))

        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=4)
        self.columnconfigure(3, weight=1)

        self.rowconfigure(1, weight=1)

    def do_background_task(self, *args):
        self.controller.do_background_task()
