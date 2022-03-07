from sqlalchemy import create_engine
import tkinter as tk
from apps.resources.variables import *
from apps.resources.container import Container

#sql_statement = """SELECT FROM Books"""

#table_df = pd.read_sql(
#    sql_statement,
#    con=engine
#)
#table_df

class BookWithdraw(Container):
    def __init__(self, root):
        super().__init__(root, "Book withdrawal menu")
        self.init_image()

        #Instructions
        instructions = tk.Label(self.container, text='To Remove Outdated Books From System, Please Enter Required Information Below:',
                                fg='black', bg='#c5e3e5', relief='raised', width=80, height=3)
        instructions.config(font=(FONT, FONT_SIZE, STYLE))
        instructions.place(relx=0.5, rely=0.09, anchor="center")

        #accession
        accession = tk.Label(self.container, text = "Accession Number", fg='black', bg='#afc8c9',
                             relief='raised', width=30, height=2)
        accession.config(font=(FONT, FONT_SIZE, STYLE))
        accession.place(relx=0.4, rely=0.4, anchor="center")

        e1 = tk.Entry(root)
        e1.place(relx=0.6, rely=0.5)

        #withdrawing
        add = tk.Button(self.container, text='Withdraw Book',
                        command=lambda:[self.container.grid_forget(), BookWithdrawSuccess(root, e1.get())],
                        bg='#c5e3e5', width=30, height=1,
                             relief='raised', borderwidth=5)
        add.config(font=(FONT, FONT_SIZE, STYLE))
        add.place(relx=0.3, rely=0.63, anchor="center") 

        #home
        home_btn = tk.Button(root, text='Back to Books Menu', command=lambda:[self.container.grid_forget(), BooksLandingPage(root)],
                             bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.7, rely=0.82, anchor="center")

        root.mainloop()
        


class BookWithdrawSuccess(Container):
    def __init__(self, root, accessionNo):
        super().__init__(root, "Book Menu")
        self.init_image()

        
        
        #insert sql code here to determine book on loan/ book on reservation/ success
        #sql_statement = "Select * FROM fines WHERE memberid = '{}'".format(self.ID_entry.get())
        #    data_fine = self.cursor.execute(sql_statement).fetchall()
        #    if len(data_fine) > 0:
        #        self.go_to_fineError

        #sql code to retrieve accessionNo, title, authors, isbn, publisher, year
                
        self.success(self.root,"a","b","c","d","e","f")

        root.mainloop()

    #book on loan failure
    def bookonloan(self, master):
        instructions = tk.Label(self.container, text='Error! Book is currently on Loan.', fg='black', bg='#FF0000',
                               relief='raised', width=60, height=3)
        instructions.config(font=(FONT, FONT_SIZE, STYLE))
        instructions.place(relx=0.5, rely=0.4, anchor="center")

        #back to withdrawal button
        home_btn = tk.Button(self.container, text='Back to Withdrawal Function', command=lambda:[self.container.grid_forget(), BookWithdraw(self.root)],
                                     bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.5, rely=0.7, anchor="center")

    #book on reservation
    def bookonreserve(self, master):
        instructions = tk.Label(self.container, text='Error! Book is currently Reserved.', fg='black', bg='#FF0000',
                               relief='raised', width=60, height=3)
        instructions.config(font=(FONT, FONT_SIZE, STYLE))
        instructions.place(relx=0.5, rely=0.4, anchor="center")

        #back to withdrawal button
        home_btn = tk.Button(self.container, text='Back to Withdrawal Function', command=lambda:[self.container.grid_forget(), BookWithdraw(self.root)],
                                     bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.5, rely=0.7, anchor="center")
    

    def success(self, master, accessionNo, title, authors, isbn, publisher, year): 
        #success text box
        success = tk.Label(self.container,
                    text='Please Confirm Details to Be Correct\n\nAccession No.: {}\nTitle: {}\nAuthors: {}\nISBN: {}\nPublisher: {}\nYear: {}'.format(accessionNo, title, authors, isbn, publisher, year),
                           fg='black', bg='#00FF00', relief='raised', width=60, height=9)
        success.config(font=(FONT, FONT_SIZE, STYLE))
        success.place(relx=0.5, rely=0.4, anchor="center")
        
        #confirm withdrawal button
        b1 = tk.Button(self.container, text="Confirm Withdrawal",
                    command=lambda:[self.container.grid_forget(), self.SQLWithdraw(accessionNo, title, authors, isbn, publisher, year), BookWithdraw(self.root)],
                                     bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        b1.config(font=(FONT, FONT_SIZE, STYLE))
        b1.place(relx=0.3, rely=0.7, anchor="center")

        #back to withdrawal button
        home_btn = tk.Button(self.container, text="Back to Withdrawal Function",
                    command=lambda:[self.container.grid_forget(), BookWithdraw(self.root)],
                                     bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.7, rely=0.7, anchor="center")
            
    def SQLWithdraw(self, accessionNo, title, authors, isbn, publisher, year):
        print("test")
        #sql code to delete book


