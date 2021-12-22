
class MainDisplayController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def calculate(self, *args):
        try:
            value = float(self.view.feet.get())
            self.view.meters.set(str(int(0.3048 * value * 10000.0 + 0.5) / 10000.0))

        except ValueError:
            pass



"""import threading
import time


class App(threading.Thread):
    def __init__(self, event_generator, update_event, finish_event):
        threading.Thread.__init__(self)
        self.update_event = update_event
        self.finish_event = finish_event
        self.event_generator = event_generator
        self.start()

    def run(self):
        print('Stuff in background ! ')
        print(threading.get_ident())
        time.sleep(5)
        print('Throwing event')
        self.event_generator(self.finish_event)
"""