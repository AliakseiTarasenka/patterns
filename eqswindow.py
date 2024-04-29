from tkinter import Toplevel, Button
from creational.abstractfactory import *


class Extra(Toplevel):
    """" Extra window for equalizers"""

    def __init__(self):
        super().__init__()
        self.title("EQs")
        self.geometry("640x480")
        self.buttons = []
        # initialize button on extra window, it will create buttons using Factory method
        self.button = Button(self, text='Show EQs', command=self.show_EQs)
        self.button.pack(expand=True)

    def show_EQs(self):
        eqsFactory = EQsFactory()

        eqs = eqsFactory.eqs
        for e in eqs:
            if e.name not in self.buttons:
                self.button = Button(self, text=f'{e.name}')
                self.button.pack(expand=True)
                self.buttons.append(e.name)
