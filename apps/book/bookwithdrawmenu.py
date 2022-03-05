from sqlalchemy import create_engine
import tkinter as tk
import bookinsert
from bookwithdraw import BookWithdrawSuccess
from apps.resources.variables import *
from apps.resources.container import Container

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
