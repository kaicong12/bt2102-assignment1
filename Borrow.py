

from tkinter import *
from textwrap import wrap
from PIL import Image, ImageTk
from sqlalchemy import text
from apps.resources.variables import *
from apps.resources.container import Container

class Borrow(Container):
    def __init__(self, root, title):
        super().__init__(root, "BorrowPage")
        self.init_image()
        #Create title label
        self.label = Label(self.container, text='To Borrow a Book, Please Enter Information Below:', fg='black', bg='#2dccb6',
                           relief='raised', width=60, height=3)
        self.label.config(font=(FONT, FONT_SIZE, STYLE))
        self.label.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align

        #Create Accession Number Label
        anLabel = Label(root, text="Accession Number")
        anLabel.place(relx=0.3, rely=0.3)
        #Entry/Input for Accession Number
        anEntry = Entry(root)
        anEntry.place(relx=0.5,rely=0.3)

        #Create Membership ID Label
        idLabel = Label(root, text="Membership ID")
        idLabel.place(relx=0.3, rely=0.4)
        #Entry/Input for Membership ID
        idEntry = Entry(root)
        idEntry.place(relx=0.5,rely=0.4)

        #Create Borrow book button
        borrowButton = Button(self.container, text="Borrow Book", padx=20, pady=20, command=self.popup) 
        borrowButton.place(relx=0.3, rely=0.8, anchor="center")

        #Create Back to Loans Menu Button
        #toLoansButton = Button(self.container, text="Back to Loans Menu", padx=20, pady=20) #Command = Go to loans menu  
        #toLoansButton.place(relx=0.6, rely=0.8, anchor="center")

        # back to loans_menu button
        self.return_btn = Button(self.container, text='Back to Loans Menu', command=self.go_to_error,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
        self.return_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.return_btn.place(relx=0.7, rely=0.9, anchor="center")
    
    def popup(self):
        self.popupPromptLabel = Label(self.container, text="Confirm Loan Details To Be Correct\n\n\n\n\n Accession Number\n Book Title\n Borrow Date\n Membership ID\n Member Name\n Due Date", 
        width = 60, height=25)
        self.popupPromptLabel.place(relx=0.5, rely=0.4, anchor="center")
        self.confirmLoanButton = Button(self.container, text="Confirm Loan", padx=20, pady=20, 
        command=self.close_and_error, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
        self.confirmLoanButton.place(relx=0.4, rely=0.65, anchor="center")
        self.backBorrowButton = Button(self.container, text="Back to Borrow Function", padx=20, pady=20, 
        command=self.close, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
        self.backBorrowButton.place(relx=0.6, rely=0.65, anchor="center")

    def close(self):
        self.backBorrowButton.lower()
        self.popupPromptLabel.lower()
        self.confirmLoanButton.lower()
        
        

    
    def close_and_error(self):
        self.popupPromptLabel.lower()
        self.confirmLoanButton.lower()
        self.backBorrowButton.lower()
        
        #If book out on loan error
        #CHECK (AccessionNo. NOT IN (SELECT AccessionNo. FROM Loan WHERE ReturnedDate IS NULL))
        
        self.LoanErrorLabel = Label(self.container, text="Error!\n\n Book currently on Loan until:\n DD/MM/YYYY", 
        width = 45, height=20)
        self.LoanErrorLabel.place(relx=0.5, rely=0.4, anchor="center")
        self.backBorrowButton = Button(self.container, text="Back to Borrow Function", padx=20, pady=20, 
        command=self.close_popupError, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
        self.backBorrowButton.place(relx=0.5, rely=0.6, anchor="center")

        #If member quota error
        self.QuotaErrorLabel = Label(self.container, text="Error!\n\n Member loan quota exceeded", 
        width = 45, height=20)
        self.QuotaErrorLabel.place(relx=0.5, rely=0.4, anchor="center")
        self.backBorrowButton = Button(self.container, text="Back to Borrow Function", padx=20, pady=20, 
        command=self.close_popupError, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
        self.backBorrowButton.place(relx=0.5, rely=0.6, anchor="center")

        #If member has outstanding fines
        self.FinesErrorLabel = Label(self.container, text="Error!\n\n Member has outstanding fines.", 
        width = 45, height=20)
        self.FinesErrorLabel.place(relx=0.5, rely=0.4, anchor="center")
        self.backBorrowButton = Button(self.container, text="Back to Borrow Function", padx=20, pady=20, 
        command=self.close_popupError, bg="#27c0ab",borderwidth=5, highlightthickness=4, highlightbackground="#ecb606", relief="raised")
        self.backBorrowButton.place(relx=0.5, rely=0.6, anchor="center")
 
     
        
    
    def close_popupError(self):
        self.LoanErrorLabel.lower()
        #self.QuotaErrorLabel.lower()
        self.FinesErrorLabel.lower()
        self.backBorrowButton.lower()
        
        
    def go_to_loan(self):
        Borrow(self.root, self.parent, self.engine)
        self.container.grid_forget()   


    



root = Tk()
app = Borrow(root, "BorrowPage")
root.mainloop()