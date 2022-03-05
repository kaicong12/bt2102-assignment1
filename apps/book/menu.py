from sqlalchemy import create_engine
import tkinter as tk
import variables, success
from variables import *

class bookinsert():
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        root.title("Book aquisition menu")

        self.container = tk.Frame(root, bg='white', width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.container.grid()

        #Instructions
        instructions = tk.Label(self.container, text='For New Book Acquisition, Please Enter Required Information Below:', fg='black', bg='#c5e3e5',
                           relief='raised', width=60, height=3)
        instructions.config(font=(FONT, FONT_SIZE, STYLE))
        instructions.place(relx=0.5, rely=0.05, anchor="center")
        

        #accession
        accession = tk.Label(self.container, text = "Accession Number", fg='black', bg='#afc8c9',
                             relief='raised', width=30, height=2)
        accession.config(font=(FONT, FONT_SIZE, STYLE))
        accession.place(relx=0.4, rely=0.17, anchor="center")

        e1 = tk.Entry(root)
        e1.place(relx=0.6, rely=0.19)

        #title
        title = tk.Label(self.container, text = "Title", fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        title.config(font=(FONT, FONT_SIZE, STYLE))
        title.place(relx=0.4, rely=0.24, anchor="center")
        
        e2 = tk.Entry(root)
        e2.place(relx=0.6, rely=0.28)

        #authors 
        authors = tk.Label(self.container, text = "Authors", fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        authors.config(font=(FONT, FONT_SIZE, STYLE))
        authors.place(relx=0.4, rely=0.31, anchor="center")
        
        e3 = tk.Entry(root)
        e3.place(relx=0.6, rely=0.37)

        #isbn
        isbn = tk.Label(self.container, text = "ISBN", fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        isbn.config(font=(FONT, FONT_SIZE, STYLE))
        isbn.place(relx=0.4, rely=0.38, anchor="center")
        
        e4 = tk.Entry(root)
        e4.place(relx=0.6, rely=0.46)

        #publisher
        publisher = tk.Label(self.container, text = "Publisher",  fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        publisher.config(font=(FONT, FONT_SIZE, STYLE))
        publisher.place(relx=0.4, rely=0.45, anchor="center")
        
        e5 = tk.Entry(root)
        e5.place(relx=0.6, rely=0.55)

        #publication year
        publication_year = tk.Label(self.container, text = "Publication Year", fg='black', bg='#afc8c9', relief='raised', width=30, height=2)
        publication_year.config(font=(FONT, FONT_SIZE, STYLE))
        publication_year.place(relx=0.4, rely=0.52, anchor="center")
        
        e6 = tk.Entry(root)
        e6.place(relx=0.6, rely=0.64)

        #adding
        add = tk.Button(self.container, text='Add New Book',
                        command=lambda:success.BookInsertionSuccess(e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()),
                        bg='#c5e3e5', width=30, height=1,
                             relief='raised', borderwidth=5)
        add.config(font=(FONT, FONT_SIZE, STYLE))
        add.place(relx=0.3, rely=0.60, anchor="center") 

        #home
        home_btn = tk.Button(root, text='Back to Books Menu', command=lambda:self.return_to_books_menu(),
                             bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.7, rely=0.78, anchor="center")

        root.mainloop()

    #returning home
    def return_to_books_menu():
        return false 
    
