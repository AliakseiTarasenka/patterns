from tkinter import *
from creational.singleton import Singleton
import eqswindow


class Window(Tk, Singleton):
    def init(self):
        print('calling from __init__ for the instance')
        super().__init__()
        # initialize button on main window, it will create extra window on click
        self.button = Button(self, text='Open EQs window', command=self.create_window_eqs)
        self.button.pack(expand=True)

    def create_window_eqs(self):
        global extraWindow
        extraWindow = eqswindow.Extra()

    def __init__(self):
        print('calling from __init__ class constructor to initialize instance')
