from sqlalchemy import create_engine
import tkinter as tk
<<<<<<< Updated upstream

root = tk.Tk()

def success():
    success_txt = tk.StringVar()
    text_box = tk.Text(root, height = 10, width = 10, padx = 15, pady = 15)
    text_box.insert(1.0, sueccess_txt)
    text_box.tag_configure("centre", justify = "centre")
    text_box.tag_add("centre", 1.0, "end")
    text_box.grid(column = 1, row = 3)
    success.txt.set("Success! New Book added in library")
=======
from variables import *

class BookInsertionSuccess():
    def __init__(self, root):
        
        self.root = root
        root.title("Book aquisition success!")
        root.geometry('400x300')

        #Textbox
        mesage = '''Success! New book added into library'''

        success_box = tk.Text(root, width=60, height=20)
        success_box.pack(expand=True)
        success_box.insert('end', message)
        success_box.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#17a1d5')

        #main menu button
        home_btn = tk.Button(root, text='Back to Acquisition Function', command=self.root.destroy,
                                 bg='#c5e3e5', width=5, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.5, rely=0.7, anchor="center")  # return_btn is always mid align
>>>>>>> Stashed changes
