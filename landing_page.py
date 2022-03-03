from tkinter import Label, Button

from apps.report.report_main import Report
from apps.resources.variables import *
from apps.resources.container import Container


class LandingPage(Container):
    def __init__(self, root):
        super().__init__(root, 'Library System Landing Page')
        self.init_image()

        # reports option
        self.report_image = self.open_image('apps/resources/reports.png', LANDING_PAGE_ICON_SIZE, LANDING_PAGE_ICON_SIZE)
        self.report_button = Button(root, image=self.report_image, command=self.go_to_report)
        self.report_button.place(relx=0.7, rely=0.7, anchor='center')
        self.report_text = Label(root, text='Reports', font=(FONT, LANDING_PAGE_FONT_SIZE, STYLE), fg='black', bg='white')
        self.report_text.place(relx=0.7, rely=0.9, anchor='center')

    def go_to_report(self):
        Report(self.root)
        self.container.grid_forget()


