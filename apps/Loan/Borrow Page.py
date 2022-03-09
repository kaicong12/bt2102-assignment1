from tkinter import *
'''
Create Menu
Textbox to indicate “To Borrow a Book, Please Enter Information Below”
User input Accession Number
User input Membership ID
Button to bring to Borrow confirm page
Button to go back to Loans Menu
'''
root = Tk()
root.title("Borrow Page")

#Create Prompt label
BorrowPromptLabel = Label(root, text="To Borrow a Book, Please Enter Information Below:")
BorrowPromptLabel.grid(row=0, column=6)

#Create Accession Number Label
anLabel = Label(root, text="Accession Number")
anLabel.grid(row=3, column=0)
#Entry/Input for Accession Number
anEntry = Entry(root)
anEntry.grid(row=3,column=4)

#Create Membership ID Label
idLabel = Label(root, text="Membership ID")
idLabel.grid(row=4, column=0)
#Entry/Input for Membership ID
idEntry = Entry(root)
idEntry.grid(row=4,column=4)

#Create Borrow Book Button
bbButton = Button(root, text="Borrow Book", padx=20,pady=20) #command=)
bbButton.grid(row=5, column=2)

#Create Back to Loans Menu Button
toLoansButton = Button(root, text="Back to Loans Menu", padx=20,pady=20) #command=go to borrow page)
toLoansButton.grid(row=5, column=7)
#Use .get to make use of input

#Notification if book on loan
Button(root)

def book_on_loan(self):
    print('Book')







root.mainloop()