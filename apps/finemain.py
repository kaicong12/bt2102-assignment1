from sqlalchemy import create_engine
import tkinter as tk
import pandas as pd
from apps.resources.variables import *
from apps.resources.container import Container
import datetime as dt

USER = 'root'
PASSWORD = 'joansoh17'
HOST = '127.0.0.1'
PORT = 3306
DATABASE = 'Library'

engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
            USER, PASSWORD, HOST, PORT, DATABASE))

sql_statement = """SELECT FROM Fines"""

class FineLandingPage(Container):
    def __init__(self, root):
        super().__init__(root, "Fine Menu")
        self.init_image()

        #book image
        self.book = self.open_image('apps/resources/fine.png', SIDE_IMAGE_WIDTH, SIDE_IMAGE_HEIGHT)
        self.book_image  = tk.Label(self.container, image=self.book)
        self.book_image.place(relx=0.25, rely=0.45, anchor='center')

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
        self.cursor = engine.connect()

        #Instructions
        self.instructions = tk.Label(self.container, text='To Pay a Fine, Please Enter Information Below:',
                                fg='black', bg='#c5e3e5', relief='raised', width=80, height=3)
        self.instructions.config(font=(FONT, FONT_SIZE, STYLE))
        self.instructions.place(relx=0.5, rely=0.09, anchor="center")

        #membership id
        self.membership = tk.Label(self.container, text = "Membership ID", fg='black', bg='#afc8c9',
                             relief='raised', width=30, height=2)
        self.membership.config(font=(FONT, FONT_SIZE, STYLE))
        self.membership.place(relx=0.4, rely=0.25, anchor="center")

        self.e1 = tk.Entry(root)
        self.e1.place(relx=0.6, rely=0.31)
        self.MemberID = self.e1.get()

        #payment date
        self.PaymentDate = tk.Label(self.container, text = "Payment Date", fg='black', bg='#afc8c9',
                             relief='raised', width=30, height=2)
        self.PaymentDate.config(font=(FONT, FONT_SIZE, STYLE))
        self.PaymentDate.place(relx=0.4, rely=0.35, anchor="center")

        self.Date = dt.datetime.now()

        self.TodayDate = tk.Label(self.container, text =f"{self.Date:%B, %d, %Y}", fg='black', bg='white',
                             width=23, height=2)
        self.TodayDate.config(font=(FONT, 15, STYLE))
        self.TodayDate.place(relx=0.64, rely=0.35, anchor="center")
        

        #payment amount
        self.PaymentAmount = tk.Label(self.container, text = "Payment Amount", fg='black', bg='#afc8c9',
                             relief='raised', width=30, height=2)
        self.PaymentAmount.config(font=(FONT, FONT_SIZE, STYLE))
        self.PaymentAmount.place(relx=0.4, rely=0.45, anchor="center")

        self.e3 = tk.Entry(root)
        self.e3.place(relx=0.6, rely=0.56)
        self.PaymentAmt = self.e3.get()


        #pay fine
        self.pay = tk.Button(self.container, text='Pay Fine',
                        command=lambda:[self.container.grid_forget(), self.FinePayment()],
                        bg='#c5e3e5', width=30, height=1,
                             relief='raised', borderwidth=5)
        self.pay.config(font=(FONT, FONT_SIZE, STYLE))
        self.pay.place(relx=0.3, rely=0.64, anchor="center") 

        #home
        self.home_btn = tk.Button(root, text='Back to Fines Menu',
                             command=lambda:[self.container.grid_forget(), FineLandingPage(root)],
                             bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        self.home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.home_btn.place(relx=0.7, rely=0.84, anchor="center")

        root.mainloop()

    def FinePayment(self):
        #confirmation text box
        self.confirm = tk.Label(self.container,
                    text='Please Confirm Details to Be Correct\n\nPayment due: {}\n(Exact Fee only)\nMember ID: {}\nPayment Date: {}'.format(self.MemberID, self.Date, self.PaymentAmt),
                           fg='black', bg='#00FF00', relief='raised', width=60, height=9)
        self.confirm.config(font=(FONT, FONT_SIZE, STYLE))
        self.confirm.place(relx=0.5, rely=0.4, anchor="center")

        #sql code there to check if member has fine/ whether payment amount correct/ success
        sql_statement = "SELECT * FROM Fine WHERE memberid = '{}'".format(self.MemberID)
        data_fine = self.cursor.execute(sql_statement).fetchall()
        if len(data_fine) > 0: #whether member has fine
            sql_statement2 = "SELECT amount FROM Fine WHERE memberid = '{}'".format(self.MemberID)
            data_amt = self.cursor.execute(sql_statement2).fetchall()
            if data_amt == PaymentAmount: #whether payment amount correct
                return self.success()
            else:
                return self.failedincorrectamt()
        else:
            return self.failednofine()

        #back to fine button
        self.return_btn = tk.Button(self.container, text="Back to Payment Function",
                    command=lambda:[self.container.grid_forget(), FinePayment(self.root)],
                                     bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        self.return_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.return_btn.place(relx=0.7, rely=0.7, anchor="center")
        
    #member has fine and correct amount 
    def success(self, master, MembershipID, PaymentDate, PaymentAmount):
        self.b1 = tk.Button(self.container, text="Confirm Payment",
                    command=lambda:[self.CloseConfirmPage(), self.SQLPay(), FinePayment(self.root)],
                                     bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        self.b1.config(font=(FONT, FONT_SIZE, STYLE))
        self.b1.place(relx=0.3, rely=0.7, anchor="center")

    #member has no fine
    def failednofine(self):
        self.b1 = tk.Button(self.container, text="Confirm Payment",
                    command=lambda:[self.CloseConfirmPage(), self.nofine(self.root)],
                                     bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        self.b1.config(font=(FONT, FONT_SIZE, STYLE))
        self.b1.place(relx=0.3, rely=0.7, anchor="center")

    #incorrect fine amount
    def failedincorrectamt(self):
        self.b1 = tk.Button(self.container, text="Confirm Payment",
                    command=lambda:[self.CloseConfirmPage(), self.incorrectamt(self.root)],
                                     bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        self.b1.config(font=(FONT, FONT_SIZE, STYLE))
        self.b1.place(relx=0.3, rely=0.7, anchor="center")
        
        
    #SQL queries to delete fine
    def SQLPay(self):
        sql_statement3 = "DELETE FROM Fine WHERE 'memberid' = '{}'".format(self.MemberID)
        self.cursor.execute(sql_statement3)

        

        sql_statement4 = "INSERT INTO Payment VALUES (%s, %s, %s)"
        self.cursor.execute(sql_statement4, (self.MemberID, accessionNo, self.Date))

    def nofine(self):
        self.ErrorPop = tk.Label(self.container, text='Error! Member has no fine.', fg='black', bg='#FF0000',
                               relief='raised', width=60, height=3)
        self.ErrorPop.config(font=(FONT, FONT_SIZE, STYLE))
        self.ErrorPop.place(relx=0.5, rely=0.4, anchor="center")

        #back to payment button
        self.back_btn = tk.Button(self.container, text='Back to Payment Function', command=lambda:[self.CloseErrorPage, self.FinePayment()],
                                     bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        self.back_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.back_btn.place(relx=0.5, rely=0.7, anchor="center")

    def incorrectamt(self):
        self.ErrorPop = tk.Label(self.container, text='Error! Incorrect fine payment amount', fg='black', bg='#FF0000',
                               relief='raised', width=60, height=3)
        self.ErrorPop.config(font=(FONT, FONT_SIZE, STYLE))
        self.ErrorPop.place(relx=0.5, rely=0.4, anchor="center")

         #back to payment button
        self.back_btn = tk.Button(self.container, text='Back to Payment Function', command=lambda:[self.CloseErrorPage, self.FinePayment()],
                                     bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        self.back_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.back_btn.place(relx=0.5, rely=0.7, anchor="center")

    #close Error page
    def CloseErrorPage(self):
        self.ErrorPop.lower()
        self.back_btn.lower()
        
    #close Confirmation Page
    def CloseConfirmPage(self):
        self.confirm.lower()
        self.return_btn.lower()
        self.b1.lower()
        


root = tk.Tk()
fine_landing_page = FineLandingPage(root)
root.mainloop()

