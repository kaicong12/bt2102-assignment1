from sqlalchemy import create_engine
import tkinter as tk


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

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)
        e5.grid(row=4, column=1)
        e6.grid(row=5, column=1)

    
        tk.Button(top, text='Back to books menu', command=top.destroy).grid(row=6, column=0, sticky=tk.W, pady=4)
        tk.Button(top, text='Add new book', command=show_entry_fields).grid(row=6, column=1, sticky=tk.W, pady=4)

        tk.mainloop()
        
    except TypeError:
        print("test")
    
