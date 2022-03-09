from sqlalchemy import create_engine
import tkinter as tk
from PIL import Image, ImageTk
from apps.resources.variables import *
from apps.resources.container import Container


USER = 'root'
PASSWORD = 'joansoh17'
HOST = '127.0.0.1'
PORT = 3306
DATABASE = 'Library'

engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
            USER, PASSWORD, HOST, PORT, DATABASE))

cursor = engine.connect()


class BookLandingPage(Container):
    def __init__(self, root):
        super().__init__(root, "Book Menu")
        self.init_image()
        self.engine = engine
        self.cursor = engine.connect()


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
        self.engine = engine
        self.root = root
        self.cursor = engine.connect()


        #Instructions
        self.instructions = tk.Label(self.container, text='For New Book Acquisition, Please Enter Required Information Below:', fg='black', bg='#c5e3e5',
                           relief='raised', width=60, height=3)
        self.instructions.config(font=(FONT, FONT_SIZE, STYLE))
        self.instructions.place(relx=0.5, rely=0.09, anchor="center")
        

        #accession
        self.accession_lbl = tk.Label(self.container, text = "Accession Number", fg='black', bg='#afc8c9',
                             relief='raised', width=30, height=2)
        self.accession_lbl.config(font=(FONT, FONT_SIZE, STYLE))
        self.accession_lbl.place(relx=0.4, rely=0.21, anchor="center")

        self.e1 = tk.Entry(root)
        self.e1.place(relx=0.6, rely=0.25)
        self.accessionNo = self.e1.get()

        #title
        self.title_lbl = tk.Label(self.container, text = "Title", fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        self.title_lbl.config(font=(FONT, FONT_SIZE, STYLE))
        self.title_lbl.place(relx=0.4, rely=0.28, anchor="center")
        
        self.e2 = tk.Entry(root)
        self.e2.place(relx=0.6, rely=0.34)
        self.title = self.e2.get()

        #authors 
        self.authors_lbl = tk.Label(self.container, text = "Authors", fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        self.authors_lbl.config(font=(FONT, FONT_SIZE, STYLE))
        self.authors_lbl.place(relx=0.4, rely=0.35, anchor="center")
        
        self.e3 = tk.Entry(root)
        self.e3.place(relx=0.6, rely=0.43)
        self.authors = self.e3.get()

        #isbn
        self.isbn_lbl = tk.Label(self.container, text = "ISBN", fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        self.isbn_lbl.config(font=(FONT, FONT_SIZE, STYLE))
        self.isbn_lbl.place(relx=0.4, rely=0.42, anchor="center")
        
        self.e4 = tk.Entry(root)
        self.e4.place(relx=0.6, rely=0.52)
        self.isbn = self.e4.get()

        #publisher
        self.publisher_lbl = tk.Label(self.container, text = "Publisher",  fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        self.publisher_lbl.config(font=(FONT, FONT_SIZE, STYLE))
        self.publisher_lbl.place(relx=0.4, rely=0.49, anchor="center")
        
        self.e5 = tk.Entry(root)
        self.e5.place(relx=0.6, rely=0.61)
        self.publisher = self.e5.get()

        #publication year
        self.publication_year_lbl = tk.Label(self.container, text = "Publication Year", fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        self.publication_year_lbl.config(font=(FONT, FONT_SIZE, STYLE))
        self.publication_year_lbl.place(relx=0.4, rely=0.56, anchor="center")
        
        self.e6 = tk.Entry(root)
        self.e6.place(relx=0.6, rely=0.70)
        self.publication_year = self.e6.get()

        #adding
        self.add = tk.Button(self.container, text='Add New Book',
                        command=lambda:self.BookInsertion(),
                             relief='raised', borderwidth=5)
        self.add.config(font=(FONT, FONT_SIZE, STYLE))
        self.add.place(relx=0.3, rely=0.70, anchor="center") 

        #home
        self.home_btn = tk.Button(root, text='Back to Books Menu', command=lambda:[self.container.grid_forget(),BookLandingPage(self.root)],
                             bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        self.home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.home_btn.place(relx=0.7, rely=0.82, anchor="center")

        root.mainloop()
        
    def BookInsertion(self):
        self.cursor = self.engine.connect()

 
        sql_statement = "SELECT * FROM books WHERE accession_no = %s"
        data_book = cursor.execute(sql_statement,(self.accessionNo,)).fetchall()

        #checking for missing or incomplete fields
        listOfInputs = [self.accessionNo, self.title, self.authors, self.isbn, self.publisher, self.publication_year]
        if "" in listOfInputs: #checks missing
            return self.failed()
        elif len(data_book) > 0: #check for duplicate
            return self.failed()
        else:
            return self.success()

    def failed(self):
        #failure text box
        self.ErrorPop = tk.Label(self.container, text='Error!\n\n Book already added;\n Duplicate, Missing or\nIncomplete fields.',
                                fg='yellow', bg='#FF0000',
                               relief='raised', width=30, height=15)
        self.ErrorPop.config(font=(FONT, FONT_SIZE, STYLE))
        self.ErrorPop.place(relx=0.5, rely=0.4, anchor="center")
        self.ErrorPop.lift()

        #back to acquisition button
        self.return_btn = tk.Button(self.container, text='Back to\nAcquisition\nFunction',
                             command=lambda:[self.ErrorPop.lower(),self.return_btn.lower()],
                                     bg='#c5e3e5', width=12, height=3, relief='raised', borderwidth=5)
        self.return_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.return_btn.place(relx=0.5, rely=0.55, anchor="center")

    def success(self):
        #insert into book table
        query = "INSERT INTO books (accession_no, title, isbn, publisher, publication_year) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (self.accessionNo, self.title, self.isbn, self.publisher, self.publication_year))

        #insert into author table
        authors = authors.split(",")
        author_name = author[0]
        query2 = "INSERT INTO book_author (author_name, book_accession) VALUES (%s, %s)"
        self.cursor.execute(query2, (author_name, self.accessionNo))
    
        if authors[1] != '':
            cursor.execute(query, (author[1], self.accession_no))
    
        if authors[2] != '':
            cursor.execute(query, (author[2], self.accession_no))
    
        #success text box
        self.SuccessPop = tk.Label(self.container, text='Success! New book added in Library', fg='black', bg='#00FF00',
                               relief='raised', width=60, height=3)
        self.SuccessPop.config(font=(FONT, FONT_SIZE, STYLE))
        self.SuccessPop.place(relx=0.5, rely=0.4, anchor="center")

        #back to acquisition button
        self.return_btn = tk.Button(self.container, text='Back to Acquisition Function',
                             command=lambda:[self.SuccessPop.lower(), self.return_btn.lower()],
                                     bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        self.return_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.return_btn.place(relx=0.5, rely=0.7, anchor="center")

    
    
    def closeError(self):
        self.instructions.lower()
        self.e1.lower()
        self.accession_lbl.lower()
        self.e2.lower()
        self.title_lbl.lower()
        self.e3.lower()
        self.authors_lbl.lower()
        self.e4.lower()
        self.isbn_lbl.lower()
        self.e5.lower()
        self.publisher_lbl.lower()
        self.e6.lower()
        self.publication_year_lbl.lower()
        self.add.lower()
        self.home_btn.lower()
        
        self.ErrorPop.lower()
        self.return_btn.lower()


#Withdrawal

class BookWithdraw(Container):
    def __init__(self, root):
        super().__init__(root, "Book withdrawal menu")
        self.init_image()
        self.init_image()
        self.parent = parent
        self.engine = engine
        self.cursor = engine.connect()


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
        self.init_image()
        self.parent = parent
        self.engine = engine
        self.cursor = engine.connect()


        #sql code here to determine book on loan/ book on reservation/ success
        sql_statement = "SELECT * FROM loan WHERE BorrowedBookAccession = '{}'".format(accessionNo)
        data_loan = self.cursor.execute(sql_statement).fetchall()
        sql_statement2 = "SELECT * FROM Reservation WHERE ReservedBookAccession = '{}'".format(accessionNo)
        data_reserve = self.cursor.execute(sql_statement2).fetchall()
        if len(data_fine) > 0:
            return self.bookonloan(self.root)
        elif len(data_reserve) > 0:
            return self.bookonreserve(self.root)
        else:
            return self.success()

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
    

    def success(self):
        #retrieving from sql
        sql_statement = "Select * FROM books WHERE 'accession_no' = '{}'".format(self.accessionNo)
        book_data = cursor.execute(sql_statement).fetchall()
        title = book_data[1]
        isbn = book_data[2]
        publisher = book_data[3]
        publication_year = book_data[4]

        sql_statement2 = "Select * from book_author WHERE 'book_accession' = '{}'".format(self.accessionNo)
        bookauthors_data = cursor.execute(sql_statement2).fetchall()
        authors_string = bookauthors_data[0][0]
        for author in bookauthors_data:
            authors_string += String.format(", %s", author[0])
        
        #success text box
        success = tk.Label(self.container,
                    text='Please Confirm Details to Be Correct\n\nAccession No.: {}\nTitle: {}\nAuthors: {}\nISBN: {}\nPublisher: {}\nYear: {}'.format(self.accessionNo, title, authors_string, isbn, publisher, year),
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
        self.cursor.execute(sql_statement3)

        sql_statement4 = "DELETE from book_author WHERE 'book_accession' = '{}'".format(accessionNo)
        self.cursor.execute(sql_statement4)

root = tk.Tk()
book_landing_page = BookLandingPage(root)
root.mainloop()
