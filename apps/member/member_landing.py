#from textwrap import wrap
from multiprocessing import parent_process
from tkinter import Label, Button, Entry, Tk, ttk, Canvas, Frame
from PIL import Image, ImageTk
from sqlalchemy import engine_from_config, text
from sqlalchemy.exc import IntegrityError, DataError
from apps.resources.variables import *
from apps.resources.container import Container

class Membership(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, 'Member Main Menu')
        self.init_image()
        self.parent = parent
        self.engine = engine

        # title label
        self.label = Label(self.container, text='Select one of the options below:', fg='black', bg='#2dccb6',
                           relief='raised', width=60, height=3)
        self.label.config(font=(FONT, FONT_SIZE, STYLE))
        self.label.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align
        
        # back to main_menu button
        self.return_btn = Button(self.container, text='Back to Main Menu', command=lambda: parent.return_to_main_menu(self),
                                 bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        self.return_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.return_btn.place(relx=0.5, rely=0.9, anchor="center")  # return_btn is always mid align

        # Membership Creation
        self.member_create_btn = Button(self.container, text='1. Membership Creation', command=self.go_to_create_member,
                            height=3, width=20, wraplength=200)
        self.member_create_btn.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#17a1d5')
        self.member_create_btn.place(relx=BUTTON_X, rely=0.16)

        # Membership Deletion
        self.member_delete_btn = Button(self.container, text='2. Membership Deletion', command=self.gp_to_delete_member,
                                height=3, width=20, wraplength=200)
        self.member_delete_btn.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#2964e7')
        self.member_delete_btn.place(relx=BUTTON_X, rely=0.32)

        # Membership Deletion
        self.member_update_btn = Button(self.container, text='3. Membership Update', command=self.go_to_update_member,
                                height=3, width=20, wraplength=200)
        self.member_update_btn.config(font=(FONT, FONT_SIZE, STYLE), fg='white', bg='#4e3ddc')
        self.member_update_btn.place(relx=BUTTON_X, rely=0.48)

    def go_to_create_member(self):
        MemberCreate(self.root, self.parent, self.engine)
        self.container.grid_forget()
    
    def gp_to_delete_member(self):
        print("Delete Member")

    def go_to_update_member(self):
        print("Update Member")

class MemberCreate(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, "Create Member Menu")
        self.init_image()
        self.parent = parent
        self.engine = engine

        # Title Label
        self.label = Label(self.container, text='To Create Member, Please Enter Requested Information Below', fg='black', bg='#2dccb6',
                    relief='raised', width=60, height=3)
        self.label.config(font=(FONT, FONT_SIZE, STYLE))
        self.label.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align

        # back to report_menu button
        self.return_btn = Button(self.container, text='Back to Main Menu', command=self.go_to_membership,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
        self.return_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.return_btn.place(relx=0.7, rely=0.9, anchor="center")

        # book search button
        self.create_member_btn = Button(self.container, text='Create Member', command=self.create_member,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
        self.create_member_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.create_member_btn.place(relx=0.3, rely=0.9, anchor="center")

        # Membership ID box
        self.ID_box = Label(self.container, text='Membership ID', bg='#1391c1', fg='white', height=3, width=20)
        self.ID_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.ID_box.place(relx=MENU_LABEL_X, rely=0.23, anchor='center')
        self.ID_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.ID_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.23, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        # Name box
        self.name_box = Label(self.container, text='Name', bg='#1fa4df', fg='white', height=3, width=20)
        self.name_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.name_box.place(relx=MENU_LABEL_X, rely=0.36, anchor='center')
        self.name_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.name_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.36, anchor='center',
                               width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        # Faculty box
        self.faculty_box = Label(self.container, text='Faculty', bg='#49abde', fg='white', height=3, width=20)
        self.faculty_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.faculty_box.place(relx=MENU_LABEL_X, rely=0.49, anchor='center')
        self.faculty_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.faculty_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.49, anchor='center',
                                width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        # Phone Number box
        self.phone_box = Label(self.container, text='Phone Number', bg='#71b6df', fg='white', height=3, width=20)
        self.phone_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.phone_box.place(relx=MENU_LABEL_X, rely=0.62, anchor='center')
        self.phone_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.phone_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.62, anchor='center',
                                width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

        # Email box
        self.email_box = Label(self.container, text='Email Address', bg='#96c4e3', fg='white', height=3, width=20)
        self.email_box.config(font=(FONT, FONT_SIZE, STYLE))
        self.email_box.place(relx=MENU_LABEL_X, rely=0.75, anchor='center')
        self.email_ent = Entry(self.container, font=(FONT, FONT_SIZE, STYLE))
        self.email_ent.place(relx=REPORT_ENTRY_BOX_X, rely=0.75, anchor='center',
                                width=REPORT_ENTRY_BOX_WIDTH, height=REPORT_ENTRY_BOX_HEIGHT)

    def go_to_membership(self):
        Membership(self.root, self.parent, self.engine)
        self.container.grid_forget()

    def popup(self, response:bool):
        if response:
            popup_text = "Success!\n\n\nALS Membership created."
            popup_bg = "#9ddd58"
            popup_font_color = "#000000"
        
        else:
            popup_text = "Error!\n\n\nMember already exist; Missing or Incomplete fields."
            popup_bg = "#cc0505"
            popup_font_color = "#ffff00"

        self.popup_label = Label(self.container, text=popup_text, bg =popup_bg, fg=popup_font_color, width=40, height=15, wraplength=450)
        self.popup_label.config(font=(FONT,FONT_SIZE, STYLE))
        self.popup_label.place(relx=0.5, rely=0.5, anchor="center")

        self.return_to_create_btn = Button(self.container, text='Back to Create Function', padx=20, pady=20,\
            command=self.close, bg='#27c0ab', borderwidth=5, relief='raised', highlightthickness=4, highlightbackground='#fae420')
        self.return_to_create_btn.config(font=(FONT,FONT_SIZE,STYLE))
        self.return_to_create_btn.place(relx=0.5, rely=0.7, anchor='center')

    def close(self):
        self.popup_label.lower()
        self.return_to_create_btn.lower()

    
    def get_entry(self):
        raw = [self.ID_ent.get(), self.name_ent.get(), self.faculty_ent.get(), self.phone_ent.get(), self.email_ent.get()]
        for item in raw:
            if item == "":
                raise ValueError('Invalid Fields: Entries cannot be empty')
        return raw

    def create_member(self):
        try:
            cursor = self.engine.connect()
            data = self.get_entry()
            sql_statement = """INSERT INTO members VALUES("{}", "{}", "{}", "{}", "{}")""".format(data[0], data[1], data[2], data[3], data[4])
            cursor.execute(sql_statement)
            self.popup(True)

        except (IntegrityError, DataError, ValueError):
            self.popup(False)

class MemberCreate(Container):
    def __init__(self, root, parent, engine):
        super().__init__(root, "Create Member Menu")
        self.init_image()
        self.parent = parent
        self.engine = engine

        # Title Label
        self.label = Label(self.container, text='To Create Member, Please Enter Requested Information Below', fg='black', bg='#2dccb6',
                    relief='raised', width=60, height=3)
        self.label.config(font=(FONT, FONT_SIZE, STYLE))
        self.label.place(relx=HEADING_LABEL_X, rely=HEADING_LABEL_Y, anchor="center")  # label is always mid align

        # back to report_menu button
        self.return_btn = Button(self.container, text='Back to Main Menu', command=self.go_to_membership,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
        self.return_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.return_btn.place(relx=0.7, rely=0.9, anchor="center")

        # book search button
        self.create_member_btn = Button(self.container, text='Create Member', command=self.create_member,
                                 bg='#27c0ab', width=20, height=2, relief='raised', borderwidth=5,
                                 highlightthickness=4, highlightbackground="#eaba2d")
        self.create_member_btn.config(font=(FONT, FONT_SIZE, STYLE))
        self.create_member_btn.place(relx=0.3, rely=0.9, anchor="center")