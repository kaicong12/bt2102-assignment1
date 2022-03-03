from tkinter import Button

from apps.resources.variables import *
from apps.resources.container import Container


class BookSearch(Container):
    def __init__(self, root):
        super().__init__(root, 'Book Search')
        self.init_image()

        # back to main_menu button
        self.return_btn = Button(self.container, text='Back to Main Menu', command=self.return_to_main_menu,
                                 bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        self.return_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.return_btn.place(relx=0.5, rely=0.9, anchor="center")  # return_btn is always mid align

