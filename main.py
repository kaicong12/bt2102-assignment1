from tkinter import Tk, Button, Label

from landing_page import LandingPage
from apps.resources.container import Container


class LibraryApp(Container):
    def __init__(self):
        self.root = Tk()

        self.frames = {}

        self.landing = LandingPage(self.root, self)

        self.root.mainloop()

    def return_to_main_menu(self, child):
        LandingPage(self.root, self)
        child.container.grid_forget()




app = LibraryApp()