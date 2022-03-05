from sqlalchemy import create_engine
import tkinter as tk
from apps.resources.variables import *

from apps.resources.container import Container

class BookWithdrawSuccess(Container):
    def __init__(self, root, accessionNo):
        super().__init__(root, "Book Menu")
        self.init_image()

        root.mainloop()
        
        #insert sql code here to check
        self.success()

        #book on load failure
        def bookonloan():
            instructions = tk.Label(self.container, text='Error! Book is currently on Loan.', fg='black', bg='#c5e3e5',
                               relief='raised', width=60, height=3)
            instructions.config(font=(FONT, FONT_SIZE, STYLE))
            instructions.place(relx=0.5, rely=0.5, anchor="center")

            #back to acquisition button
            home_btn = tk.Button(self.container, text='Back to Aquisition Function', command=lambda:[self.container.grid_forget(), bookinsert(root)],
                                     bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
            home_btn.config(font=(FONT, FONT_SIZE, STYLE))
            home_btn.place(relx=0.5, rely=0.7, anchor="center")

        #book on reservation
        def bookonreserve():
            instructions = tk.Label(self.container, text='Error! Book is currently Reserved.', fg='black', bg='#c5e3e5',
                               relief='raised', width=60, height=3)
            instructions.config(font=(FONT, FONT_SIZE, STYLE))
            instructions.place(relx=0.5, rely=0.5, anchor="center")

            #back to withdrawal button
            home_btn = tk.Button(self.container, text='Back to Withdrawal Function', command=lambda:[self.container.grid_forget(), BookWithdraw(root)],
                                     bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
            home_btn.config(font=(FONT, FONT_SIZE, STYLE))
            home_btn.place(relx=0.5, rely=0.7, anchor="center")
    

        def success():
            #sql code to retrieve accessionNo, title, authors, isbn, publisher, year

            #success text box
            toplevel = Toplevel(ws)
            toplevel.title("")
            toplevel.geometry("230x100")

            l2=tk.Label(toplevel,text="Please Confirm Details to Be Correct\n{}\n{}\n{}\n{}\n{}\n{}".format())
            l2.place(relx=0.5, rely=0.7, anchor="center")

            b1=Button(toplevel,text="Confirm Withdrawal",command=lambda:[self.container.grid_forget(), SQLWithdraw()], width=10)
            b1.place(relx=0.2, rely=0.7, anchor="center")
            b2=Button(toplevel,text="Back to Withdrawal Function",command=lambda:[self.container.grid_forget(), BookWithdraw(root)],
                      width=10)
            b2.place(relx=0.6, rely=0.7, anchor="center")
            
            def SQLWithdraw():
                print("test")
                #sql code to delete book
