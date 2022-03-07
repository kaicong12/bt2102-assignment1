from sqlalchemy import create_engine
import tkinter as tk
from apps.resources.variables import *
from apps.resources.container import Container

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
        home_btn = tk.Button(root, text='Back to Books Menu', command=lambda:[self.container.grid_forget(), back],
                             bg='#c5e3e5', width=30, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.7, rely=0.82, anchor="center")

        root.mainloop()

    #returning home
    def return_to_books_menu():
        return false 

class BookInsertionSuccess(Container):
    def __init__(self, root, accessionNo, title, authors, isbn, publisher, publication_year):
        super().__init__(root, "Book Menu")
        self.init_image()

        #checking for missing or incomplete fields
        listOfInputs = [accessionNo, title, authors, isbn, publisher, publication_year]
        if "" in listOfInputs:
            return self.failed
        else:
            return self.success

        #check for duplicates

        root.mainloop()

        def failed():
            #failure text box
            instructions = tk.Label(self.container, text='Error! Book already added; Duplicate, Missing or Incomplete fields.', fg='black', bg='#c5e3e5',
                               relief='raised', width=60, height=3)
            instructions.config(font=(FONT, FONT_SIZE, STYLE))
            instructions.place(relx=0.5, rely=0.5, anchor="center")

            #back to acquisition button
            home_btn = tk.Button(self.container, text='Back to Acquisition Function', command=lambda:[self.container.grid_forget(), bookinsert(root)],
                                     bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
            home_btn.config(font=(FONT, FONT_SIZE, STYLE))
            home_btn.place(relx=0.5, rely=0.7, anchor="center")
    

        def success():
            #insert sql code here
    
            #success text box
            instructions = tk.Label(self.container, text='Success! New book added in Library', fg='black', bg='#c5e3e5',
                               relief='raised', width=60, height=3)
            instructions.config(font=(FONT, FONT_SIZE, STYLE))
            instructions.place(relx=0.5, rely=0.5, anchor="center")

            #back to acquisition button
            home_btn = tk.Button(self.container, text='Back to Acquisition Function', command=lambda:[self.container.grid_forget(), bookinsert(root)],
                                     bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
            home_btn.config(font=(FONT, FONT_SIZE, STYLE))
            home_btn.place(relx=0.5, rely=0.7, anchor="center")


