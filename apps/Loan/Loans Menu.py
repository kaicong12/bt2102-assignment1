from tkinter import *


root = Tk()
root.title("Loans Menu")

#Create Menu Prompt
#menuPrompt = Entry(root, width = 30)
#menuPrompt.grid(row=0, column=1, padx=20)

#Create Prompt label
menuPromptLabel = Label(root, text="Select one of the Options below:")
menuPromptLabel.grid(row=0, column=6)

#Create Borrow book button
borrowButton = Button(root, text="Book Borrowing", padx=20,pady=20) #command=go to borrow page)
borrowButton.grid(row=3, column=10)


#Create Return book button
returnButton = Button(root, text="Book Returning",padx=20, pady=20) # command = go to return page)
returnButton.grid(row=4, column=10)

#Create Back to Menu button
mainMenuButton = Button(root, text="Back To Main Menu", padx=50) #command = go back to main menu
mainMenuButton.grid(row=10, column=6)


root.mainloop()
