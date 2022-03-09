from tkinter import *
'''
Textbox to indicate “To Return a Book, Please Enter Information Below”
User input Accession Number
User input Return Date
Button to bring to Return confirm page
Button to go back to Loans Menu

'''
root = Tk()
root.title("Return Page")

#Create Prompt label
ReturnPromptLabel = Label(root, text="To Return a Book, Please Enter Information Below:")
ReturnPromptLabel.grid(row=0, column=6)

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

#Create Return Book Button
rbButton = Button(root, text="Return Book", padx=20,pady=20) #command=go to borrow page)
rbButton.grid(row=5, column=2)

#Create Back to Loans Menu Button
toLoansButton = Button(root, text="Back to Loans Menu", padx=20,pady=20) #command=go to borrow page)
toLoansButton.grid(row=5, column=7)
#Use .get to make use of input







root.mainloop()