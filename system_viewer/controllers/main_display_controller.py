import threading
import time


class AsyncTask(threading.Thread):
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


def print_callbackl(*args):
    print('Callback : ' + str(threading.get_ident()))


class MainDisplayController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def do_background_task(self):
        print(self.view)
        print('Test before sleep and launching test')
        print_callbackl()
        self.view.bind('<<AsynCb>>', print_callbackl)

        AsyncTask(self.view.event_generate, None, '<<AsynCb>>')
