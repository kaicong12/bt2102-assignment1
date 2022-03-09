from tkinter import Label, Button

from apps.resources.variables import *
from apps.resources.container import Container
from apps.report.report_pages import Report
from finemain import FineLandingPage
from bookmain import BookLandingPage
#from apps.bookmain import BookLandingPage
#from apps.finemain import FineLandingPage

class LandingPage(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, 'Library System Landing Page')
        self.init_image()
        self.parent = parent
        self.engine = engine

        # reports option
        self.landing_report_image = self.open_image('apps/resources/reports.png', LANDING_PAGE_ICON_SIZE,
                                                    LANDING_PAGE_ICON_SIZE)
        self.report_button = Button(root, image=self.landing_report_image, command=self.go_to_report())
        self.report_button.place(relx=0.7, rely=0.7, anchor='center')
        self.report_text = Label(root, text='Reports', font=(FONT, LANDING_PAGE_FONT_SIZE, STYLE),
                                 fg='black',
                                 bg='white')
        self.report_text.place(relx=0.72, rely=0.9, anchor='center')

        # book option
        self.landing_books_image = self.open_image('apps/resources/book.png', LANDING_PAGE_ICON_SIZE,
                                                    LANDING_PAGE_ICON_SIZE)
        self.books_btn = Button(root, image=self.landing_books_image, command=self.go_to_book())
        self.books_btn.place(relx=0.5, rely=0.5, anchor='center')
        self.books_text = Label(root, text='Books', font=(FONT, LANDING_PAGE_FONT_SIZE, STYLE),
                                 fg='black',
                                 bg='white')
        self.report_text.place(relx=0.5, rely=0.9, anchor='center')

        #fine option
        self.landing_fines_image = self.open_image('apps/resources/fine.png', LANDING_PAGE_ICON_SIZE,
                                                    LANDING_PAGE_ICON_SIZE)
        self.fines_btn = Button(root, image=self.landing_fines_image, command=self.go_to_fine())
        self.fines_btn.place(relx=0.7, rely=0.9, anchor='center')
        self.fines_text = Label(root, text='Fines', font=(FONT, LANDING_PAGE_FONT_SIZE, STYLE),
                                 fg='black',
                                 bg='white')
        self.fines_text.place(relx=0.3, rely=0.9, anchor='center')

    def go_to_report(self):
        Report(self.root, self.parent, self.engine)
        self.container.grid_forget()

    def go_to_book(self):
        BookLandingPage(self.root, self.parent, self.engine)
        self.container.grid_forget()

    def go_to_fine(self):
        FineLandingPage(self.root, self.parent, self.engine)
        self.container.grid_forget()

