from tkinter import Tk
from apps.resources.container import Container
from tkinter import Tk
from tkinter import *
class Loan(Container):
    def __init__(self, root, title):
        super().__init__(root, "LoanPage")
        self.init_image()
        #Create Prompt label
        menuPromptLabel = Label(root, text="Select one of the Options below:")
        menuPromptLabel.grid(row=0, column=6)

#Create Borrow book button
        borrowButton = Button(root, text="Book Borrowing", padx=20,pady=20) #command=go to borrow page)
        borrowButton.grid(row=3, column=10)


root = Tk()
app = Loan(root, "LoanPage")
root.mainloop()