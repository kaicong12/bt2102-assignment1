from sqlalchemy import create_engine
import tkinter as tk
from PIL import Image, ImageTk
from apps.resources.variables import *
from apps.resources.container import Container


USER = 'root'
PASSWORD = 'joansoh17'
HOST = '127.0.0.1'
PORT = 3306
DATABASE = 'ALS'

engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
            USER, PASSWORD, HOST, PORT, DATABASE))

cursor = engine.connect()


class BookLandingPage(Container):
    def __init__(self, root):
        super().__init__(root, "Book Menu")
        self.init_image()

        #book image
        self.book = self.open_image('apps/resources/book.png', SIDE_IMAGE_WIDTH, SIDE_IMAGE_HEIGHT)
        self.book_image  = tk.Label(self.container, image=self.book)
        self.book_image.place(relx=0.25, rely=0.45, anchor='center')
        self.book_text = tk.Label(self.container, text='Books', font=(FONT, FONT_SIZE, STYLE), fg='white', bg='black')
        self.book_text.place(relx=SIDE_TEXT_X, rely=SIDE_TEXT_Y, anchor='center')

        #instructions
        instructions = tk.Label(self.container, text='Select one of the options below:', fg='black', bg='#c5e3e5',
                           relief='raised', width=60, height=3)
        instructions.config(font=(FONT, FONT_SIZE, STYLE))
        instructions.place(relx=0.5, rely=0.09, anchor="center")

        #acquisition button
        aquisition_btn = tk.Button(self.container, command = lambda:[self.container.grid_forget(), bookinsert(root)],
                                   text="Book Acquisition", bg='#c5e3e5', width=50, height=4, relief='raised', borderwidth=5)
        aquisition_btn.config(font=(FONT, FONT_SIZE, STYLE))
        aquisition_btn.place(relx=0.7, rely=0.3, anchor='center')

        #withdrawal button
        withdraw_btn = tk.Button(self.container, command = lambda:[self.container.grid_forget(), BookWithdraw(root)],
                                   text="Book Withdrawal", bg='#c5e3e5', width=50, height=4, relief='raised', borderwidth=5)
        withdraw_btn.config(font=(FONT, FONT_SIZE, STYLE))
        withdraw_btn.place(relx=0.7, rely=0.5, anchor='center')
        
        #main menu button
        home_btn = tk.Button(self.container, text='Back to Main Menu',
                                 bg='#c5e3e5', width=20, height=2, relief='raised',
                                 borderwidth=5,highlightthickness=4, highlightbackground="#eaba2d")
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.7, rely=0.68, anchor="center") 

    def return_to_main_menu(self):
        print("a")

#Insertion
class bookinsert(Container):
    def __init__(self, root):
        super().__init__(root, "Book aquisition menu")
        self.init_image()

        #Instructions
        instructions = tk.Label(self.container, text='For New Book Acquisition, Please Enter Required Information Below:', fg='black', bg='#c5e3e5',
                           relief='raised', width=60, height=3)
        instructions.config(font=(FONT, FONT_SIZE, STYLE))
        instructions.place(relx=0.5, rely=0.09, anchor="center")
        

        #accession
        accession = tk.Label(self.container, text = "Accession Number", fg='black', bg='#afc8c9',
                             relief='raised', width=30, height=2)
        accession.config(font=(FONT, FONT_SIZE, STYLE))
        accession.place(relx=0.4, rely=0.21, anchor="center")

        e1 = tk.Entry(root)
        e1.place(relx=0.6, rely=0.25)

        #title
        title = tk.Label(self.container, text = "Title", fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        title.config(font=(FONT, FONT_SIZE, STYLE))
        title.place(relx=0.4, rely=0.28, anchor="center")
        
        e2 = tk.Entry(root)
        e2.place(relx=0.6, rely=0.34)

        #authors 
        authors = tk.Label(self.container, text = "Authors", fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        authors.config(font=(FONT, FONT_SIZE, STYLE))
        authors.place(relx=0.4, rely=0.35, anchor="center")
        
        e3 = tk.Entry(root)
        e3.place(relx=0.6, rely=0.43)

        #isbn
        isbn = tk.Label(self.container, text = "ISBN", fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        isbn.config(font=(FONT, FONT_SIZE, STYLE))
        isbn.place(relx=0.4, rely=0.42, anchor="center")
        
        e4 = tk.Entry(root)
        e4.place(relx=0.6, rely=0.52)

        #publisher
        publisher = tk.Label(self.container, text = "Publisher",  fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        publisher.config(font=(FONT, FONT_SIZE, STYLE))
        publisher.place(relx=0.4, rely=0.49, anchor="center")
        
        e5 = tk.Entry(root)
        e5.place(relx=0.6, rely=0.61)

        #publication year
        publication_year = tk.Label(self.container, text = "Publication Year", fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        publication_year.config(font=(FONT, FONT_SIZE, STYLE))
        publication_year.place(relx=0.4, rely=0.56, anchor="center")
        
        e6 = tk.Entry(root)
        e6.place(relx=0.6, rely=0.70)

        #adding
        add = tk.Button(self.container, text='Add New Book',
                        command=lambda:[self.container.grid_forget(),
                                        BookInsertionSuccess(root, e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get())],
                        bg='#c5e3e5', width=30, height=1,
                             relief='raised', borderwidth=5)
        add.config(font=(FONT, FONT_SIZE, STYLE))
        add.place(relx=0.3, rely=0.63, anchor="center") 

        #home
        home_btn = tk.Button(root, text='Back to Books Menu', command=lambda:[self.container.grid_forget(), BookLandingPage(self.root)],
                             bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.7, rely=0.82, anchor="center")

        root.mainloop()


class BookInsertionSuccess(Container):
    def __init__(self, root, accessionNo, title, authors, isbn, publisher, publication_year):
        super().__init__(root, "Book Menu")
        self.init_image()

        #check for duplicate
        sql_statement = "SELECT * FROM libbooks WHERE 'Accession Number' = '{}'".format(accessionNo)
        data_book = cursor.execute(sql_statement).fetchall()

        #checking for missing or incomplete fields
        listOfInputs = [accessionNo, title, authors, isbn, publisher, publication_year]
        if "" in listOfInputs:
            return self.failed(self.root)
        elif len(data_book) > 0:
            return self.failed(self.root)
        else:
            return self.success(self.root, accessionNo, title, authors, isbn, publisher, publication_year)
        
        root.mainloop()

    def failed(self, master):
        #failure text box
        instructions = tk.Label(self.container, text='Error! Book already added; Duplicate, Missing or Incomplete fields.',
                                fg='black', bg='#FF0000',
                               relief='raised', width=60, height=3)
        instructions.config(font=(FONT, FONT_SIZE, STYLE))
        instructions.place(relx=0.5, rely=0.4, anchor="center")

        #back to acquisition button
        home_btn = tk.Button(self.container, text='Back to Acquisition Function',
                             command=lambda:[self.container.grid_forget(), bookinsert(root)],
                                     bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.5, rely=0.7, anchor="center")
    

    def success(self, master, accessionNo, title, authors, isbn, publisher, publication_year):
        #insert into book table
        query = "INSERT INTO books (accession_no, title, isbn, publisher, publication_year) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (accessionNo, title, isbn, publisher, publication_year))

        #insert into author table
        authors = authors.split(",")
        query2 = "INSERT INTO author (author_name, accessionNo) VALUES (%s, %s)"
        cursor.execture(query2, (author_name, accessionNo))
    
        if authors[1] != '':
            cursor.execute(query, (author[1], accession_no))
    
        if authors[2] != '':
            cursor.execute(query, (author[2], accession_no))
    
        #success text box
        instructions = tk.Label(self.container, text='Success! New book added in Library', fg='black', bg='#00FF00',
                               relief='raised', width=60, height=3)
        instructions.config(font=(FONT, FONT_SIZE, STYLE))
        instructions.place(relx=0.5, rely=0.4, anchor="center")

        #back to acquisition button
        home_btn = tk.Button(self.container, text='Back to Acquisition Function',
                             command=lambda:[self.container.grid_forget(), bookinsert(root)],
                                     bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.5, rely=0.7, anchor="center")


#Withdrawal

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
        home_btn = tk.Button(root, text='Back to Books Menu', command=lambda:[self.container.grid_forget(), BookLandingPage(root)],
                             bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.7, rely=0.82, anchor="center")

        root.mainloop()
        


class BookWithdrawSuccess(Container):
    def __init__(self, root, accessionNo):
        super().__init__(root, "Book Menu")
        self.init_image()

        #sql code here to determine book on loan/ book on reservation/ success
        sql_statement = "SELECT * FROM loan WHERE BorrowedBookAccession = '{}'".format(accessionNo)
        data_loan = self.cursor.execute(sql_statement).fetchall()
        sql_statement2 = "SELECT * FROM Reservation WHERE ReservedBookAccession = '{}'".format(accessionNo)
        data_reserve = self.cursor.execute(sql_statement2.fetchall()
        if len(data_fine) > 0:
            return self.bookonloan(self.root)
        elif len(data_reserve) >0:
            return self.bookonreserve(self.root)
        else:
            return self.success(self.root, accessionNo)

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
    

    def success(self, master, accessionNo):
        #retrieving from sql
        sql_statement = "Select * FROM books WHERE 'accession_no' = '{}'".format(accessionNo))
        book_data = cursor.execute(sql_statement).fetchall()
        title = book_data[1]
        isbn = book_data[2]
        publisher = book_data[3]
        publication_year = book_data[4]

        sql_statement2 = "Select * from book_author WHERE 'book_accession' = '{}'".format(accessionNo))
        bookauthors_data = cursor.execute(sql_statement2).fetchall()
        authors_string = bookauthors_data[0][0]
        for author in bookauthors_data:
            authors_string += String.format(", %s", author[0])
        
        #success text box
        success = tk.Label(self.container,
                    text='Please Confirm Details to Be Correct\n\nAccession No.: {}\nTitle: {}\nAuthors: {}\nISBN: {}\nPublisher: {}\nYear: {}'.format(accessionNo, title, authors_string, isbn, publisher, year),
                           fg='black', bg='#00FF00', relief='raised', width=60, height=9)
        success.config(font=(FONT, FONT_SIZE, STYLE))
        success.place(relx=0.5, rely=0.4, anchor="center")
        
        #confirm withdrawal button
        b1 = tk.Button(self.container, text="Confirm Withdrawal",
                    command=lambda:[self.container.grid_forget(), self.SQLWithdraw(accessionNo), BookWithdraw(self.root)],
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
        #deleting on sql
        sql_statement3 = "DELETE FROM books WHERE 'accession_no' = '{}'".format(accessionNo)
        cursor.execute(sql_statement3)

        sql_statement4 = "DELETE from book_author WHERE 'book_accession' = '{}'".format(accessionNo)
        cursor.execute(sql_statement4)


root = tk.Tk()
book_landing_page = BookLandingPage(root)
root.mainloop()
