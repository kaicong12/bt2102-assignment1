from tkinter import Tk, Frame, Label, Button
from PIL import Image, ImageTk

from apps.report.report_main import Report
from apps.resources.variables import *
from landing_page import LandingPage


LANDING_PAGE_ICON_SIZE = 300
LANDING_PAGE_FONT_SIZE = 40

class App:
    def __init__(self):
        self.root = Tk()
        self.landing_page = LandingPage(self.root)

        self.root.mainloop()



app = App()