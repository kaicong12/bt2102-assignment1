from tkinter import Label, Button
from apps.Loan.Loan import Loan
from apps.Loan.Reservation import Reservation

from apps.resources.variables import *
from apps.resources.container import Container
from apps.report.report_pages import Report


class LandingPage(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, 'Library System Landing Page')
        self.init_image()
        self.parent = parent
        self.engine = engine

        # reports option
        self.landing_report_image = self.open_image('apps/resources/reports.png', LANDING_PAGE_ICON_SIZE,
                                                    LANDING_PAGE_ICON_SIZE)
        self.report_button = Button(root, image=self.landing_report_image, command=self.go_to_report)
        self.report_button.place(relx=0.7, rely=0.7, anchor='center')
        self.report_text = Label(root, text='Reports', font=(FONT, LANDING_PAGE_FONT_SIZE, STYLE),
                                 fg='black',
                                 bg='white')
        self.report_text.place(relx=0.7, rely=0.9, anchor='center')

        
        # loan option
        self.landing_loan_image = self.open_image('apps/resources/loan.png', LANDING_PAGE_ICON_SIZE,
                                                    LANDING_PAGE_ICON_SIZE)
        self.loan_button = Button(root, image=self.landing_loan_image, command=self.go_to_loan)
        self.loan_button.place(relx=0.7, rely=0.2, anchor='center')
        self.loan_text = Label(root, text='Loans', font=(FONT, LANDING_PAGE_FONT_SIZE, STYLE),
                                 fg='black',
                                 bg='white')
        self.loan_text.place(relx=0.7, rely=0.4, anchor='center')
        
        # reservation option
        self.landing_reservation_image = self.open_image('apps/resources/reservation.png', LANDING_PAGE_ICON_SIZE,
                                                    LANDING_PAGE_ICON_SIZE)
        self.reservation_button = Button(root, image=self.landing_reservation_image, command=self.go_to_reservation)
        self.reservation_button.place(relx=0.2, rely=0.7, anchor='center')
        self.reservation_text = Label(root, text='Reservations', font=(FONT, LANDING_PAGE_FONT_SIZE, STYLE),
                                 fg='black',
                                 bg='white')
        self.reservation_text.place(relx=0.2, rely=0.9, anchor='center')
    
    def go_to_report(self):
        Report(self.root, self.parent, self.engine)
        self.container.grid_forget()
    
    def go_to_loan(self):
        Loan(self.root, self.parent, self.engine)
        self.container.grid_forget()
    
    def go_to_reservation(self):
        Reservation(self.root, self.parent, self.engine)
        self.container.grid_forget()