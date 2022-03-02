from sqlalchemy import create_engine
import tkinter as tk
import menu

#USER = 'sashimitrash'
#PASSWORD = ''
#HOST = '127.0.0.1'
#PORT = 3306
#DATABASE = 'Library'

#engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}[:{3}]/{4}'.format(USER, PASSWORD, HOST, PORT, DATABASE))
#cursor = engine.connect()

root = tk.Tk()
root.title("Book Menu")

canvas = tk.Canvas(root, width = 600, height = 400)
canvas.grid(columnspan = 3)

#instructions
instructions = tk.Label(root, text = "Select one of the Options below", font = "Arial")
instructions.grid(columnspan = 3, column = 0, row = 0)

#acquisition button
aquisition_txt = tk.StringVar()
aquisition_btn = tk.Button(root, command = lambda:menu.book(), textvariable = aquisition_txt, bg = "cyan", fg = "white", height = 4, width = 30)
aquisition_txt.set("Book Acquisition")
aquisition_btn.grid(columnspan = 2, column = 3, row = 1)

#withdrawal button
withdraw_txt = tk.StringVar()
withdraw_btn = tk.Button(root, textvariable = withdraw_txt, bg = "cyan", fg = "white", height = 4, width = 30)
withdraw_txt.set("Book Withdrawal")
withdraw_btn.grid(columnspan = 2, column = 3, row = 2)

#main menu button
home_txt = tk.StringVar()
home_btn = tk.Button(root, textvariable = home_txt, bg = "black", fg = "white", height = 4, width = 30)
home_txt.set("Back to Main Menu")
home_btn.grid(column = 0, row = 3)

canvas = tk.Canvas(root, width = 600, height = 250)
canvas.grid(columnspan = 3)
