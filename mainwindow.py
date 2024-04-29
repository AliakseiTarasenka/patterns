from tkinter import *
from creational.singleton import Singleton


class Window(Tk, Singleton):
    def init(self):
        print('calling from __init__ for the instance')
        super().__init__()

    def __init__(self):
        print('calling from __init__ class constructor')
