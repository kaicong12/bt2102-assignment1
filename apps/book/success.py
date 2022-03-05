from sqlalchemy import create_engine
import tkinter as tk
from apps.resources.variables import *

class BookInsertionSuccess:
    def __init__(self, accessionNo, title, authors, isbn, publisher, publication_year):
        win= tk.Tk()
        win.geometry("600x250")
        w = Label(root, text ='Success', font = "50") 
        w.pack()

        #insert sql code here
        messagebox.showinfo("Book aquisition success!", "Success! New book added in Library")

        win.mainloop()
