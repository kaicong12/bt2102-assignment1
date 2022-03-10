from sqlalchemy import create_engine
import tkinter as tk
import pandas as pd
from apps.resources.variables import *
from apps.resources.container import Container
import datetime as dt


class FineLandingPage(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, "Fine Menu")
        self.init_image()
        self.parent = parent
        self.engine = engine

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
        payment_btn = tk.Button(self.container, command = lambda:[self.container.grid_forget(), FinePayment(root, self.parent, self.engine)],
                                   text="Fine Payment", bg='#c5e3e5', width=50, height=4, relief='raised', borderwidth=5)
        payment_btn.config(font=(FONT, FONT_SIZE, STYLE))
        payment_btn.place(relx=0.7, rely=0.4, anchor='center')

        #main menu button
        home_btn = tk.Button(self.container, text='Back to Main Menu',
                                 command=parent.return_to_main_menu(self),
                                 bg='#c5e3e5', width=20, height=2, relief='raised',
                                 borderwidth=5,highlightthickness=4, highlightbackground="#eaba2d")
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.7, rely=0.68, anchor="center")

        root.mainloop()


class FinePayment(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, "Fine Payment Menu")
        self.init_image()
        self.parent = parent
        self.engine = engine
        self.cursor = self.engine.connect()

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
        self.e1.place(relx=0.6, rely=0.28)
        
        #payment date
        self.PaymentDate = tk.Label(self.container, text = "Payment Date", fg='black', bg='#afc8c9',
                             relief='raised', width=30, height=2)
        self.PaymentDate.config(font=(FONT, FONT_SIZE, STYLE))
        self.PaymentDate.place(relx=0.4, rely=0.35, anchor="center")

        self.TodayDate = dt.datetime.now()

        self.e2 = tk.Entry(root)
        self.e2.insert(0, f"{self.TodayDate:%B, %d, %Y}")
        self.e2.place(relx=0.6, rely=0.40)
        

        #payment amount
        self.PaymentAmount = tk.Label(self.container, text = "Payment Amount", fg='black', bg='#afc8c9',
                             relief='raised', width=30, height=2)
        self.PaymentAmount.config(font=(FONT, FONT_SIZE, STYLE))
        self.PaymentAmount.place(relx=0.4, rely=0.45, anchor="center")

        self.e3 = tk.Entry(root)
        self.e3.place(relx=0.6, rely=0.52)

        #pay fine
        self.pay = tk.Button(self.container, text='Pay Fine',
                        command=lambda:[self.ClosePayPopup, self.FinePay],
                        bg='#c5e3e5', width=30, height=1,
                             relief='raised', borderwidth=5)
        self.pay.config(font=(FONT, FONT_SIZE, STYLE))
        self.pay.place(relx=0.3, rely=0.64, anchor="center") 

        #home
        self.home2_btn = tk.Button(root, text='Back to Fines Menu',
                             command=lambda:[self.container.grid_forget, FineLandingPage(self.root, self.parent, self.engine)],
                             bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        self.home2_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.home2_btn.place(relx=0.7, rely=0.75, anchor="center")

        root.mainloop()

    def FinePay(self):
        self.MemberID = self.e1.get()
        self.Date = self.e2.get()
        self.PaymentAmt = self.e3.get()
        #confirmation text box
        txt = "Please Confirm Details to Be Correct\n\nPayment due: {}\n(Exact Fee only)\nMember ID: {}\nPayment Date: {}"
        self.confirm = tk.Label(self.container,
                                text= txt.format(self.PaymentAmt, self.MemberID, self.Date),
                                fg='black', bg='#00FF00', relief='raised', width=60, height=9)
        self.confirm.config(font=(FONT, FONT_SIZE, STYLE))
        self.confirm.place(relx=0.5, rely=0.4, anchor="center")

        #back to fine button
        self.return_btn = tk.Button(self.container, text="Back to Payment Function",
                    command=lambda:[self.CloseConfirmPage, FinePayment(self.root, self.parent, self.engine)],
                                     bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        self.return_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.return_btn.place(relx=0.7, rely=0.7, anchor="center")

        #sql code there to check if member has fine/ whether payment amount correct/ success
        sql_statement = "SELECT * FROM Fine WHERE memberid = '{}'".format(self.MemberID)
        data_fine = self.cursor.execute(sql_statement).fetchall()
        if len(data_fine) > 0: #whether member has fine
            sql_statement2 = "SELECT amount FROM Fine WHERE memberid = '{}'".format(self.MemberID)
            data_amt = self.cursor.execute(sql_statement2).fetchall()
            if data_amt == self.PaymentAmnt: #whether payment amount correct
                return self.success
            else:
                return self.failedincorrectamt
        else:
            return self.failednofine
        
    #member has fine and correct amount 
    def success(self):
        self.b1 = tk.Button(self.container, text="Confirm Payment",
                    command=lambda:[self.CloseConfirmPage, self.SQLPay, FinePayment(self.root, self.parent, self.engine)],
                                     bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        self.b1.config(font=(FONT, FONT_SIZE, STYLE))
        self.b1.place(relx=0.3, rely=0.7, anchor="center")

    #member has no fine
    def failednofine(self):
        self.b1 = tk.Button(self.container, text="Confirm Payment",
                    command=lambda:[self.CloseConfirmPage, self.nofine],
                                     bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        self.b1.config(font=(FONT, FONT_SIZE, STYLE))
        self.b1.place(relx=0.3, rely=0.7, anchor="center")

    #incorrect fine amount
    def failedincorrectamt(self):
        self.b1 = tk.Button(self.container, text="Confirm Payment",
                    command=lambda:[self.CloseConfirmPage, self.incorrectamt],
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
        self.back_btn = tk.Button(self.container, text='Back to Payment Function', command=lambda:[self.CloseErrorPage, FinePayment(self.root, self.parent, self.engine)],
                                     bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        self.back_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.back_btn.place(relx=0.5, rely=0.7, anchor="center")

    def incorrectamt(self):
        self.ErrorPop = tk.Label(self.container, text='Error! Incorrect fine payment amount', fg='black', bg='#FF0000',
                               relief='raised', width=60, height=3)
        self.ErrorPop.config(font=(FONT, FONT_SIZE, STYLE))
        self.ErrorPop.place(relx=0.5, rely=0.4, anchor="center")

         #back to payment button
        self.back_btn = tk.Button(self.container, text='Back to Payment Function', command=lambda:[self.CloseErrorPage, FinePayment(self.root, self.parent, self.engine)],
                                     bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        self.back_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.back_btn.place(relx=0.5, rely=0.7, anchor="center")

    #close Error page
    def CloseErrorPage(self):
        self.ErrorPop.lower
        self.back_btn.lower
        
    #close Confirmation Page
    def CloseConfirmPage(self):
        self.confirm.lower
        self.return_btn.lower
        self.b1.lower

    def ClosePayPopup(self):
        self.instructions.lower
        self.membership.lower
        self.e1.lower
        self.PaymentDate.lower
        self.e2.lower
        self.PaymentAmount.lower
        self.e3.lower
        self.pay.lower
        self.home2_btn.lower
        
        

