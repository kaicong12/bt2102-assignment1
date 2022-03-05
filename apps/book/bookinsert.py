from sqlalchemy import create_engine
import tkinter as tk
from apps.resources.variables import *
from apps.resources.container import Container

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
            home_btn = tk.Button(self.container, text='Back to Aquisition Function', command=lambda:[self.container.grid_forget(), bookinsert(root)],
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
            home_btn = tk.Button(self.container, text='Back to Aquisition Function', command=lambda:[self.container.grid_forget(), bookinsert(root)],
                                     bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
            home_btn.config(font=(FONT, FONT_SIZE, STYLE))
            home_btn.place(relx=0.5, rely=0.7, anchor="center")

