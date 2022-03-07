from sqlalchemy import create_engine
import tkinter as tk
from PIL import Image, ImageTk
from bookinsertmenu import bookinsert
from bookwithdrawmenu import BookWithdraw
from apps.resources.variables import *
from apps.resources.container import Container


USER = 'root'
PASSWORD = 'joansoh17'
HOST = '127.0.0.1'
PORT = 3306
DATABASE = 'Library'

engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
            USER, PASSWORD, HOST, PORT, DATABASE))



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

root = tk.Tk()
book_landing_page = BookLandingPage(root)
root.mainloop()
