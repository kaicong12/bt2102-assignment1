from sqlalchemy import create_engine
import tkinter as tk

root = tk.Tk()

def success():
    success_txt = tk.StringVar()
    text_box = tk.Text(root, height = 10, width = 10, padx = 15, pady = 15)
    text_box.insert(1.0, sueccess_txt)
    text_box.tag_configure("centre", justify = "centre")
    text_box.tag_add("centre", 1.0, "end")
    text_box.grid(column = 1, row = 3)
    success.txt.set("Success! New Book added in library")
