from sqlalchemy import create_engine
import tkinter as tk
import pandas as pd
from apps.resources.variables import *
from apps.resources.container import Container

#USER = 'root'
#PASSWORD = 'joansoh17'
#HOST = '127.0.0.1'
#PORT = 3306
#DATABASE = 'Library'

#engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
            #USER, PASSWORD, HOST, PORT, DATABASE))

#sql_statement = """SELECT FROM Fines"""

#table_df = pd.read_sql(
#    sql_statement,
#    con=engine
#)
#table_df


class FineLandingPage(Container):
    def __init__(self, root):
        super().__init__(root, "Fine Menu")
        self.init_image()

        #book image
        self.book = self.open_image('apps/resources/fine.png', SIDE_IMAGE_WIDTH, SIDE_IMAGE_HEIGHT)
        self.book_image  = tk.Label(self.container, image=self.book)
        self.book_image.place(relx=0.25, rely=0.45, anchor='center')
        self.book_text = tk.Label(self.container, text='Books', font=(FONT, FONT_SIZE, STYLE), fg='white', bg='black')
        self.book_text.place(relx=SIDE_TEXT_X, rely=SIDE_TEXT_Y, anchor='center')

        #instructions
        instructions = tk.Label(self.container, text='Select one of the options below:', fg='black', bg='#c5e3e5',
                           relief='raised', width=60, height=3)
        instructions.config(font=(FONT, FONT_SIZE, STYLE))
        instructions.place(relx=0.5, rely=0.09, anchor="center")

        #payment button
        payment_btn = tk.Button(self.container, command = lambda:[self.container.grid_forget(), FinePayment(root)],
                                   text="Fine Payment", bg='#c5e3e5', width=50, height=4, relief='raised', borderwidth=5)
        payment_btn.config(font=(FONT, FONT_SIZE, STYLE))
        payment_btn.place(relx=0.7, rely=0.4, anchor='center')

        #main menu button
        home_btn = tk.Button(self.container, text='Back to Main Menu',
                                 bg='#c5e3e5', width=20, height=2, relief='raised',
                                 borderwidth=5,highlightthickness=4, highlightbackground="#eaba2d")
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.7, rely=0.68, anchor="center")

        root.mainloop()


class FinePayment(Container):
    def __init__(self, root):
        super().__init__(root, "Fine Payment Menu")
        self.init_image()

        #Instructions
        instructions = tk.Label(self.container, text='To Pay a Fine, Please Enter Information Below:',
                                fg='black', bg='#c5e3e5', relief='raised', width=80, height=3)
        instructions.config(font=(FONT, FONT_SIZE, STYLE))
        instructions.place(relx=0.5, rely=0.09, anchor="center")

        #membership id
        membership = tk.Label(self.container, text = "Membership ID", fg='black', bg='#afc8c9',
                             relief='raised', width=30, height=2)
        membership.config(font=(FONT, FONT_SIZE, STYLE))
        membership.place(relx=0.4, rely=0.25, anchor="center")

        e1 = tk.Entry(root)
        e1.place(relx=0.6, rely=0.31)

        #payment date
        PaymentDate = tk.Label(self.container, text = "Payment Date", fg='black', bg='#afc8c9',
                             relief='raised', width=30, height=2)
        PaymentDate.config(font=(FONT, FONT_SIZE, STYLE))
        PaymentDate.place(relx=0.4, rely=0.35, anchor="center")

        e2 = tk.Entry(root)
        e2.place(relx=0.6, rely=0.43)

        #payment amount
        PaymentAmount = tk.Label(self.container, text = "Payment Amount", fg='black', bg='#afc8c9',
                             relief='raised', width=30, height=2)
        PaymentAmount.config(font=(FONT, FONT_SIZE, STYLE))
        PaymentAmount.place(relx=0.4, rely=0.45, anchor="center")

        e3 = tk.Entry(root)
        e3.place(relx=0.6, rely=0.56)


        #pay fine
        pay = tk.Button(self.container, text='Pay Fine',
                        command=lambda:[self.container.grid_forget(), FinePaymentSuccess(self.root, e1.get(), e2.get(), e3.get())],
                        bg='#c5e3e5', width=30, height=1,
                             relief='raised', borderwidth=5)
        pay.config(font=(FONT, FONT_SIZE, STYLE))
        pay.place(relx=0.3, rely=0.64, anchor="center") 

        #home
        home_btn = tk.Button(root, text='Back to Fines Menu',
                             command=lambda:[self.container.grid_forget(), FineLandingPage(root)],
                             bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.7, rely=0.84, anchor="center")

        root.mainloop()

class FinePaymentSuccess(Container):
    def __init__(self, root, MemberID, PaymentDate, PaymentAmount):
        super().__init__(root, "Book Menu")
        self.init_image()

        #confirmation text box
        confirm = tk.Label(self.container,
                    text='Please Confirm Details to Be Correct\n\nPayment due: {}\n(Exact Fee only)\nMember ID: {}\nPayment Date: {}'.format(MemberID, PaymentDate, PaymentAmount),
                           fg='black', bg='#00FF00', relief='raised', width=60, height=9)
        confirm.config(font=(FONT, FONT_SIZE, STYLE))
        confirm.place(relx=0.5, rely=0.4, anchor="center")


        #insert sql code there to check if member has fine/ whether payment amount correct/ success
        #determines which function is run in confirm withdrawalbutton
        self.failednofine(self.root)

        #back to fine button
        home_btn = tk.Button(self.container, text="Back to Payment Function",
                    command=lambda:[self.container.grid_forget(), FinePayment(self.root)],
                                     bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.7, rely=0.7, anchor="center")
        
    #member has fine and correct amount 
    def success(self, master, MembershipID, PaymentDate, PaymentAmount):
        b1 = tk.Button(self.container, text="Confirm Payment",
                    command=lambda:[self.container.grid_forget(), self.SQLPay(self.root, MembershipID, PaymentDate, PaymentAmount), FinePayment(self.root)],
                                     bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        b1.config(font=(FONT, FONT_SIZE, STYLE))
        b1.place(relx=0.3, rely=0.7, anchor="center")

    #member has no fine
    def failednofine(self, master):
        b1 = tk.Button(self.container, text="Confirm Payment",
                    command=lambda:[self.container.grid_forget(), self.nofine(self.root)],
                                     bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        b1.config(font=(FONT, FONT_SIZE, STYLE))
        b1.place(relx=0.3, rely=0.7, anchor="center")

    #incorrect fine amount
    def failedincorrectamt(self, master):
        b1 = tk.Button(self.container, text="Confirm Payment",
                    command=lambda:[self.container.grid_forget(), self.incorrectamt(self.root)],
                                     bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        b1.config(font=(FONT, FONT_SIZE, STYLE))
        b1.place(relx=0.3, rely=0.7, anchor="center")
        
        
    #SQL queries to delete fine
    def SQLPay(self, master, MembershipID, PaymentDate, PaymentAmount):
        return "test"

    def nofine(self, master):
        instructions = tk.Label(self.container, text='Error! Member has no fine.', fg='black', bg='#FF0000',
                               relief='raised', width=60, height=3)
        instructions.config(font=(FONT, FONT_SIZE, STYLE))
        instructions.place(relx=0.5, rely=0.4, anchor="center")

    def incorrectamt(self, master):
        instructions = tk.Label(self.container, text='Error! Incorrect fine payment amount', fg='black', bg='#FF0000',
                               relief='raised', width=60, height=3)
        instructions.config(font=(FONT, FONT_SIZE, STYLE))
        instructions.place(relx=0.5, rely=0.4, anchor="center")


root = tk.Tk()
fine_landing_page = FineLandingPage(root)
root.mainloop()

