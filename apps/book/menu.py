from sqlalchemy import create_engine
import tkinter as tk
<<<<<<< Updated upstream


def book():
    top = tk.Toplevel()
    top.title("Book aquisition menu")
    
    def show_entry_fields():
        print("Accession Number: %s\nTitle: %s\nAuthors: %s\nISBN: %s\nPublisher: %s\nPublication Year: %s" % (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()))

    try:
        tk.Label(top, text = "Accession Number").grid(row = 0)
        tk.Label(top, text = "Title").grid(row = 1)
        tk.Label(top, text = "Authors").grid(row = 2)
        tk.Label(top, text = "ISBN").grid(row = 3)
        tk.Label(top, text = "Publisher").grid(row = 4)
        tk.Label(top, text = "Publication Year").grid(row = 5)

        e1 = tk.Entry(top)
        e2 = tk.Entry(top)
        e3 = tk.Entry(top)
        e4 = tk.Entry(top)
        e5 = tk.Entry(top)
        e6 = tk.Entry(top)
=======
import variables, success
from variables import *

class bookinsert():
    def __init__(self, root):
        self.root = root
        root.title("Book aquisition menu")
        

        #Labels
        tk.Label(root, text = "Accession Number").grid(row = 0) 
        tk.Label(root, text = "Title").grid(row = 1)
        tk.Label(root, text = "Authors").grid(row = 2)
        tk.Label(root, text = "ISBN").grid(row = 3)
        tk.Label(root, text = "Publisher").grid(row = 4)
        tk.Label(root, text = "Publication Year").grid(row = 5)
        
        e1 = tk.Entry(root)
        e2 = tk.Entry(root)
        e3 = tk.Entry(root)
        e4 = tk.Entry(root)
        e5 = tk.Entry(root)
        e6 = tk.Entry(root)
>>>>>>> Stashed changes

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)
        e5.grid(row=4, column=1)
        e6.grid(row=5, column=1)

<<<<<<< Updated upstream
    
        tk.Button(top, text='Back to books menu', command=top.destroy).grid(row=6, column=0, sticky=tk.W, pady=4)
        tk.Button(top, text='Add new book', command=show_entry_fields).grid(row=6, column=1, sticky=tk.W, pady=4)

        tk.mainloop()
        
    except TypeError:
        print("test")
=======
        def show_entry_fields():
            checking = [e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()]
            for ele in checking:
                if ele == "":
                    print("failure")
            print("Accession Number: %s\nTitle: %s\nAuthors: %s\nISBN: %s\nPublisher: %s\nPublication Year: %s"
                  % (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()))
            root.destroy
            success.BookInsertionSuccess(root)
    
        tk.Button(root, text='Back to books menu', command=root.destroy).grid(row=6, column=0, sticky=tk.W, pady=4)
        tk.Button(root, text='Add new book', command=show_entry_fields).grid(row=6, column=1, sticky=tk.W, pady=4)

        root.mainloop()

>>>>>>> Stashed changes
    
