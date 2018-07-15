#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Library_lending_system - main.py
# Created by JT on 06-Jul-18 23:30.
#
# author = 'JT <jiting@jtcat.com>'
import base64
import json
import codecs
import os
import tkinter.messagebox
from tkinter import *
from hashlib import sha256
from hmac import HMAC
from tkinter import ttk


class Book(object):
    def __init__(self, db):
        self.isbn = []
        self.title = []
        self.author = []
        self.pages = []
        self.published = []
        self.borrower = []
        for i in db:
            self.isbn.append(i["isbn"])
            self.title.append(i["title"])
            self.author.append(i["author"])
            self.pages.append(i["pages"])
            self.published.append(i["published"])
            if not i["borrower"]:
                self.borrower.append("-")
            else:
                self.borrower.append(i["borrower"])
        self.save()

    def save(self):
        with codecs.open("book_db.json", "w", "utf-8") as f:
            for i in range(len(self.isbn)):
                dic = {"isbn": self.isbn[i], "title": self.title[i], "author": self.author[i],
                       "pages": self.pages[i], "published": self.published[i], "borrower": self.borrower[i]}
                json.dump(dic, f, ensure_ascii=False)
                f.write('\n')


class Database(object):
    def __init__(self):
        self.user_data = []
        self.book_data = []
        self.load()

    def load(self):
        self.user_data = []
        self.book_data = []
        try:
            with codecs.open("user_db.json", "r", "utf-8") as f:
                for line in f:
                    dic1 = json.loads(line)
                    self.user_data.append(dic1)
        except FileNotFoundError:
            self.user_data = [{"username": "admin",
                               "pwd": "wiiSO/uKqonTJZl3VGanYzxyV9BWqBSR1N5/cN1+5E1JWqOpsXo4Bg==", "level": 10}]
            with codecs.open("user_db.json", "w", "utf-8") as f:
                for i in self.user_data:
                    json.dump(i, f, ensure_ascii=False)
                f.write('\n')

        try:
            with codecs.open("book_db.json", "r", "utf-8") as f:
                for line in f:
                    dic2 = json.loads(line)
                    self.book_data.append(dic2)
        except FileNotFoundError:
            self.book_data = [{"isbn": 9780321714114, "title": "C++ Primer (5th Edition)",
                               "author": "Stanley B. Lippman", "pages": 976, "published": 2012, "borrower": "-"},
                              {"isbn": 9780321928429, "title": "C Primer Plus (6th Edition)", "author": "Stephen Prata",
                               "pages": 1080, "published": 2013, "borrower": "-"},
                              {"isbn": 9780316129084, "title": "Leviathan Wakes", "author": "James S.A. Corey",
                               "pages": 592, "published": 2011, "borrower": "-"},
                              {"isbn": 9780553380163, "title": "A Brief History of Time (10th Edition)",
                               "author": "Stephen Hawking", "pages": 212, "published": 1998, "borrower": "-"}]

    @staticmethod
    def encrypt_pass(pwd, salt=None):
        if not salt:
            salt = os.urandom(8)
        else:
            # self.salt = self.salt.encode("utf-8")
            pass

        pwd = pwd.encode('UTF-8')

        hashed = pwd
        for i in range(10):
            hashed = HMAC(hashed, salt, sha256).digest()

        return salt + hashed

    def check_pwd(self, hashed, input_password):
        salt = hashed[:8]
        return hashed == self.encrypt_pass(input_password, salt)

    def validate_login(self, username, password):
        user_number = len(self.user_data)
        try_number = 0
        for i in range(user_number):
            if username == self.user_data[i]["username"]:
                try_number += 1
                success = data.check_pwd(base64.b64decode(self.user_data[i]["pwd"]), password)
                if success:
                    return True, self.user_data[i]["level"]
                else:
                    return False
        if try_number == 0:
            return False


class Library(object):
    def __init__(self, top=None):
        self.user = ""
        self.user_level = 0
        self.selected = []
        self.like = ttk.Style()
        if sys.platform == "win32":
            self.like.theme_use('vista')
        self.like.configure('.', background="#BBDEFB", foreground='#212121', font="TkDefaultFont")
        self.like.map('.', background=[('selected', "#d9d9d9"), ('active', '#BBDEFB')])

        top.geometry("960x576+200+100")
        top.title("Library self-service lending system")
        top.configure(background="#BBDEFB")
        top.configure(highlightbackground="#BBDEFB")
        top.configure(highlightcolor="black")

        self.menu_bar = Menu(top, font="TkMenuFont", bg="#BBDEFB", fg='#212121')
        top.configure(menu=self.menu_bar)

        self.menu_bar.add_command(
            activebackground="#BBDEFB",
            activeforeground="#212121",
            background="#BBDEFB",
            font="TkMenuFont",
            foreground="#212121",
            label="Sign in",
            command=lambda: self.sign_in())
        self.menu_bar.add_command(
            activebackground="#BBDEFB",
            activeforeground="#212121",
            background="#BBDEFB",
            font="TkMenuFont",
            foreground="#212121",
            label="Register",
            command=lambda: self.register())
        self.menu_bar.add_command(
            activebackground="#BBDEFB",
            activeforeground="#212121",
            background="#BBDEFB",
            font="TkMenuFont",
            foreground="#212121",
            label="Sign out",
            command=lambda: self.sign_out(),
            state=DISABLED)
        self.menu_bar.add_command(
            activebackground="#BBDEFB",
            activeforeground="#212121",
            background="#BBDEFB",
            font="TkMenuFont",
            foreground="#212121",
            label="Exit",
            command=lambda: top.destroy())

        self.add_book_button = Button(top)
        self.add_book_button.place(relx=0.02, rely=0.03, relheight=0.125, relwidth=0.11)
        self.add_book_button.configure(activebackground="#BBDEFB")
        self.add_book_button.configure(activeforeground="#212121")
        self.add_book_button.configure(background="#BBDEFB")
        self.add_book_button.configure(disabledforeground="#a3a3a3")
        self.add_book_button.configure(foreground="#212121")
        self.add_book_button.configure(highlightbackground="#BBDEFB")
        self.add_book_button.configure(highlightcolor="black")
        self.add_book_button.configure(pady="0")
        self.add_book_button.configure(text='''Add new book''')
        self.add_book_button.configure(command=lambda: self.add_book(), state=DISABLED)

        self.remove_book_button = Button(top)
        self.remove_book_button.place(relx=0.15, rely=0.03, relheight=0.125, relwidth=0.11)
        self.remove_book_button.configure(activebackground="#BBDEFB")
        self.remove_book_button.configure(activeforeground="#212121")
        self.remove_book_button.configure(background="#BBDEFB")
        self.remove_book_button.configure(disabledforeground="#a3a3a3")
        self.remove_book_button.configure(foreground="#212121")
        self.remove_book_button.configure(highlightbackground="#BBDEFB")
        self.remove_book_button.configure(highlightcolor="black")
        self.remove_book_button.configure(pady="0")
        self.remove_book_button.configure(text='''Remove book''')
        self.remove_book_button.configure(command=lambda: self.remove_book(), state=DISABLED)

        self.search_entry = Entry(top)
        self.search_entry.place(relx=0.29, rely=0.1, height=31, relwidth=0.3)
        self.search_entry.configure(background="white")
        self.search_entry.configure(font="TkFixedFont")
        self.search_entry.configure(disabledforeground="#a3a3a3")
        self.search_entry.configure(foreground="#212121")
        self.search_entry.configure(highlightbackground="#BBDEFB")
        self.search_entry.configure(highlightcolor="black")
        self.search_entry.configure(insertbackground="black")
        self.search_entry.configure(selectbackground="#c4c4c4")
        self.search_entry.configure(selectforeground="black", state=DISABLED)

        self.search_button = Button(top)
        self.search_button.place(relx=0.6, rely=0.1, height=33, width=76)
        self.search_button.configure(activebackground="#BBDEFB")
        self.search_button.configure(activeforeground="#212121")
        self.search_button.configure(background="#BBDEFB")
        self.search_button.configure(disabledforeground="#a3a3a3")
        self.search_button.configure(foreground="#212121")
        self.search_button.configure(highlightbackground="#BBDEFB")
        self.search_button.configure(highlightcolor="black")
        self.search_button.configure(pady="0")
        self.search_button.configure(text='''Search''')
        self.search_button.configure(command=lambda: self.search(), state=DISABLED)

        self.borrow_button = Button(top)
        self.borrow_button.place(relx=0.71, rely=0.03, relheight=0.125, relwidth=0.11)
        self.borrow_button.configure(activebackground="#BBDEFB")
        self.borrow_button.configure(activeforeground="#212121")
        self.borrow_button.configure(background="#BBDEFB")
        self.borrow_button.configure(disabledforeground="#a3a3a3")
        self.borrow_button.configure(foreground="#212121")
        self.borrow_button.configure(highlightbackground="#BBDEFB")
        self.borrow_button.configure(highlightcolor="black")
        self.borrow_button.configure(pady="0")
        self.borrow_button.configure(text='''Borrow''')
        self.borrow_button.configure(command=lambda: self.borrowed(), state=DISABLED)

        self.return_button = Button(top)
        self.return_button.place(relx=0.85, rely=0.03, relheight=0.125, relwidth=0.11)
        self.return_button.configure(activebackground="#BBDEFB")
        self.return_button.configure(activeforeground="#212121")
        self.return_button.configure(background="#BBDEFB")
        self.return_button.configure(disabledforeground="#a3a3a3")
        self.return_button.configure(foreground="#212121")
        self.return_button.configure(highlightbackground="#BBDEFB")
        self.return_button.configure(highlightcolor="black")
        self.return_button.configure(pady="0")
        self.return_button.configure(text='''Return''')
        self.return_button.configure(command=lambda: self.returned(), state=DISABLED)

        self.tree_view = ttk.Treeview(top)
        self.bar = ttk.Scrollbar(top, orient="vertical", command=self.tree_view.yview)
        self.bar.place(relx=0.96, rely=0.19, relheight=0.78)
        self.tree_view.place(relx=0.02, rely=0.19, relheight=0.78, relwidth=0.94)
        columns = ("ISBN", "Title", "Author", "Pages", "Published Year", "Borrower")
        self.tree_view.configure(columns=columns)
        self.tree_view.configure(yscrollcommand=self.bar.set, show='headings')
        self.tree_view.heading("ISBN", text="ISBN")
        self.tree_view.heading("ISBN", anchor="center")
        self.tree_view.column("ISBN", width="70")
        self.tree_view.column("ISBN", minwidth="70")
        self.tree_view.column("ISBN", stretch="1")
        self.tree_view.column("ISBN", anchor="center")
        self.tree_view.heading("Title", text="Title")
        self.tree_view.heading("Title", anchor="center")
        self.tree_view.column("Title", width="250")
        self.tree_view.column("Title", minwidth="200")
        self.tree_view.column("Title", stretch="1")
        self.tree_view.column("Title", anchor="center")
        self.tree_view.heading("Author", text="Author")
        self.tree_view.heading("Author", anchor="center")
        self.tree_view.column("Author", width="110")
        self.tree_view.column("Author", minwidth="90")
        self.tree_view.column("Author", stretch="1")
        self.tree_view.column("Author", anchor="center")
        self.tree_view.heading("Pages", text="Pages")
        self.tree_view.heading("Pages", anchor="center")
        self.tree_view.column("Pages", width="40")
        self.tree_view.column("Pages", minwidth="40")
        self.tree_view.column("Pages", stretch="1")
        self.tree_view.column("Pages", anchor="center")
        self.tree_view.heading("Published Year", text="Published Year")
        self.tree_view.heading("Published Year", anchor="center")
        self.tree_view.column("Published Year", width="60")
        self.tree_view.column("Published Year", minwidth="60")
        self.tree_view.column("Published Year", stretch="1")
        self.tree_view.column("Published Year", anchor="center")
        self.tree_view.heading("Borrower", text="Borrower")
        self.tree_view.heading("Borrower", anchor="center")
        self.tree_view.column("Borrower", width="80")
        self.tree_view.column("Borrower", minwidth="80")
        self.tree_view.column("Borrower", stretch="1")
        self.tree_view.column("Borrower", anchor="center")
        self.bar.config(command=self.tree_view.yview())
        self.tree_view.bind('<ButtonRelease-1>', self.treeview_click)

        for col in columns:
            self.tree_view.heading(col, text=col,
                                   command=lambda _col=col: self.treeview_sort_column(self.tree_view, _col, False))

        self.notice_label = Label(top)
        self.notice_label.place(relx=0.29, rely=0.03, height=30, width=80)
        self.notice_label.configure(background="#BBDEFB")
        self.notice_label.configure(disabledforeground="#a3a3a3")
        self.notice_label.configure(foreground="#212121")
        self.notice_label.configure(text="Please Sign in!")

        self.notice_l2 = Label(top)
        self.notice_l2.place(relx=0.40, rely=0.03, height=30, width=90)
        self.notice_l2.configure(background="#BBDEFB")
        self.notice_l2.configure(disabledforeground="#a3a3a3")
        self.notice_l2.configure(foreground="#212121")
        self.notice_l2.configure(text='''Managed user :''')

        self.managed_user = Entry(top)
        self.managed_user.place(relx=0.5, rely=0.03, height=30, relwidth=0.17)
        self.managed_user.configure(background="white")
        self.managed_user.configure(disabledforeground="#a3a3a3")
        self.managed_user.configure(font="TkFixedFont")
        self.managed_user.configure(foreground="#212121")
        self.managed_user.configure(insertbackground="black")
        self.managed_user.configure(width=204)
        self.managed_user.configure(state=DISABLED)

    def load_data(self):
        self.notice_label.configure(text="Hi, %s" % self.user)
        self.tree_view.delete(*self.tree_view.get_children())
        search_str = str(self.search_entry.get()).lower()
        show_list = []
        search_list = [book.isbn, book.title, book.author, book.pages, book.published, book.borrower]
        x = 0
        if search_str != "":
            for item in search_list:
                for length in range(len(item)):
                    if x == 0:
                        i = str(item[length])
                        if search_str in i:
                            show_list.append(length)
                    if x == 1:
                        i = str(item[length]).lower()
                        if search_str in i:
                            show_list.append(length)
                    if x == 2:
                        i = str(item[length]).lower()
                        if search_str in i:
                            show_list.append(length)
                    if x == 3:
                        i = str(item[length])
                        if search_str in i:
                            show_list.append(length)
                    if x == 4:
                        i = str(item[length])
                        if search_str in i:
                            show_list.append(length)
                    if x == 5:
                        i = str(item[length]).lower()
                        if search_str in i:
                            show_list.append(length)
                x += 1
            show_list = list(set(show_list))
            for i in show_list:
                self.tree_view.insert("", "end", values=(book.isbn[i], book.title[i], book.author[i],
                                                         book.pages[i], book.published[i], book.borrower[i]))
        else:
            count = len(book.isbn)
            for i in range(count):
                self.tree_view.insert("", "end", values=(book.isbn[i], book.title[i], book.author[i],
                                                         book.pages[i], book.published[i], book.borrower[i]))

    def treeview_click(self, event):
        print(event)
        for item in self.tree_view.selection():
            item_text = self.tree_view.item(item, "values")
            # print(item_text)
            self.selected = item_text

    def treeview_sort_column(self, tv, col, reverse):
        li = [(tv.set(k, col), k) for k in tv.get_children('')]
        try:
            li.sort(key=lambda t: int(t[0]), reverse=reverse)
        except ValueError:
            li.sort(reverse=reverse)
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(li):
            tv.move(k, '', index)
            print(k)
        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))

    def search(self):
        self.load_data()

    @staticmethod
    def add_book():
        def adding(isbn, title, author, pages, publish):
            if len(isbn) != 13:
                tkinter.messagebox.showinfo("Info", "Parameter error!\nISBN can only be 13 digits.")
            elif title == "":
                tkinter.messagebox.showinfo("Info", "Parameter error!\nPlease enter the title of the book.")
            elif author == "":
                tkinter.messagebox.showinfo("Info", "Parameter error!\nPlease enter the author of the book.")
            elif not pages:
                tkinter.messagebox.showinfo("Info", "Parameter error!\nPlease enter the pages of the book.")
            elif not publish:
                tkinter.messagebox.showinfo("Info", "Parameter error!\nPlease enter the published year of the book.")
            else:
                book.isbn.append(int(isbn))
                book.title.append(title)
                book.author.append(author)
                book.pages.append(pages)
                book.published.append(publish)
                book.borrower.append("-")
                book.save()
                main.load_data()
                tkinter.messagebox.showinfo("Info", "Successfully added!")
                add_book.destroy()

        add_book = Toplevel(root)
        add_book.geometry("378x382+531+206")
        add_book.title("Adding book...")
        add_book.configure(background="#BBDEFB")

        l1 = Label(add_book)
        l1.place(relx=0.03, rely=0.05, height=36, width=102)
        l1.configure(background="#BBDEFB")
        l1.configure(disabledforeground="#a3a3a3")
        l1.configure(foreground="#212121")
        l1.configure(text='''ISBN:''')
        l1.configure(width=102)

        e1 = Entry(add_book)
        e1.place(relx=0.32, rely=0.04, height=41, relwidth=0.62)
        e1.configure(background="white")
        e1.configure(disabledforeground="#a3a3a3")
        e1.configure(font="TkFixedFont")
        e1.configure(foreground="#212121")
        e1.configure(insertbackground="black")
        e1.configure(width=234)

        l2 = Label(add_book)
        l2.place(relx=0.03, rely=0.18, height=36, width=98)
        l2.configure(background="#BBDEFB")
        l2.configure(disabledforeground="#a3a3a3")
        l2.configure(foreground="#212121")
        l2.configure(text='''Title:''')
        l2.configure(width=98)

        e2 = Entry(add_book)
        e2.place(relx=0.32, rely=0.18, height=41, relwidth=0.62)
        e2.configure(background="white")
        e2.configure(disabledforeground="#a3a3a3")
        e2.configure(font="TkFixedFont")
        e2.configure(foreground="#212121")
        e2.configure(insertbackground="black")
        e2.configure(width=234)

        label3 = Label(add_book)
        label3.place(relx=0.03, rely=0.33, height=36, width=94)
        label3.configure(background="#BBDEFB")
        label3.configure(disabledforeground="#a3a3a3")
        label3.configure(foreground="#212121")
        label3.configure(text='''Author:''')
        label3.configure(width=94)

        entry3 = Entry(add_book)
        entry3.place(relx=0.32, rely=0.32, height=41, relwidth=0.62)
        entry3.configure(background="white")
        entry3.configure(disabledforeground="#a3a3a3")
        entry3.configure(font="TkFixedFont")
        entry3.configure(foreground="#212121")
        entry3.configure(insertbackground="black")
        entry3.configure(width=234)

        label4 = Label(add_book)
        label4.place(relx=0.03, rely=0.48, height=36, width=92)
        label4.configure(background="#BBDEFB")
        label4.configure(disabledforeground="#a3a3a3")
        label4.configure(foreground="#212121")
        label4.configure(text='''Pages:''')
        label4.configure(width=92)

        entry4 = Entry(add_book)
        entry4.place(relx=0.32, rely=0.47, height=41, relwidth=0.62)
        entry4.configure(background="white")
        entry4.configure(disabledforeground="#a3a3a3")
        entry4.configure(font="TkFixedFont")
        entry4.configure(foreground="#212121")
        entry4.configure(insertbackground="black")
        entry4.configure(width=234)

        label5 = Label(add_book)
        label5.place(relx=0.03, rely=0.63, height=36, width=106)
        label5.configure(background="#BBDEFB")
        label5.configure(disabledforeground="#a3a3a3")
        label5.configure(foreground="#212121")
        label5.configure(text='''Published Year:''')
        label5.configure(width=106)

        entry5 = Entry(add_book)
        entry5.place(relx=0.32, rely=0.62, height=41, relwidth=0.62)
        entry5.configure(background="white")
        entry5.configure(disabledforeground="#a3a3a3")
        entry5.configure(font="TkFixedFont")
        entry5.configure(foreground="#212121")
        entry5.configure(insertbackground="black")
        entry5.configure(width=234)

        button1 = Button(add_book)
        button1.place(relx=0.53, rely=0.79, height=53, width=116)
        button1.configure(activebackground="#BBDEFB")
        button1.configure(activeforeground="#212121")
        button1.configure(background="#BBDEFB")
        button1.configure(disabledforeground="#a3a3a3")
        button1.configure(foreground="#212121")
        button1.configure(highlightbackground="#BBDEFB")
        button1.configure(highlightcolor="black")
        button1.configure(pady="0")
        button1.configure(text='''Submit''')
        button1.configure(width=116)
        button1.configure(command=lambda: adding(e1.get(), e2.get(), entry3.get(),
                                                 int(entry4.get()), int(entry5.get())))

    def remove_book(self):
        if not self.selected:
            pass
        else:
            index = book.isbn.index(int(self.selected[0]))
            if book.borrower[index] == "-":
                book.isbn.pop(index)
                book.title.pop(index)
                book.author.pop(index)
                book.pages.pop(index)
                book.published.pop(index)
                book.borrower.pop(index)
                book.save()
                main.load_data()
                tkinter.messagebox.showinfo("Info", "Successfully removed the selected book!")
            else:
                tkinter.messagebox.showinfo("Info", "This book is currently being borrowed and cannot be removed.")

    def borrowed(self):
        managed_user = self.managed_user.get()
        if self.user_level == 10:
            if managed_user in book.borrower:
                tkinter.messagebox.showinfo("Info", "You can't help %s borrow this book!\n"
                                                    "Reason: Each one can only borrow a book." % managed_user)
            elif managed_user != "" and managed_user not in book.borrower:
                book.borrower[book.isbn.index(int(self.selected[0]))] = managed_user
                tkinter.messagebox.showinfo("Info", "You successfully borrowed this book.")
                self.load_data()
                book.save()
            elif self.user in book.borrower and managed_user == "":
                tkinter.messagebox.showinfo("Info", "You can't borrow this book!\n"
                                                    "Reason: You have already borrowed another book.")
            else:
                book.borrower[book.isbn.index(int(self.selected[0]))] = self.user
                tkinter.messagebox.showinfo("Info", "You successfully borrowed this book.")
                self.load_data()
                book.save()
        else:
            if self.user in book.borrower:
                tkinter.messagebox.showinfo("Info", "You can't borrow this book!\n"
                                                    "Reason: You have already borrowed another book.")
            elif self.selected[5] != "-":
                tkinter.messagebox.showinfo("Info", "You can't borrow this book!\n"
                                                    "Reason: This book has been borrowed by others.")
            else:
                book.borrower[book.isbn.index(int(self.selected[0]))] = self.user
                tkinter.messagebox.showinfo("Info", "You successfully borrowed this book.")
                self.load_data()
                book.save()

    def returned(self):
        managed_user = self.managed_user.get()
        if self.user not in book.borrower and managed_user == "":
            tkinter.messagebox.showinfo("Info", "You can't return this book!\n"
                                                "Reason: You haven't borrowed any book.")
        elif self.selected[5] != self.user and self.user_level != 10:
            tkinter.messagebox.showinfo("Info", "You can't return this book!\n"
                                                "Reason: This book is not borrowed by you..")
        elif self.user_level == 10:
            if managed_user in book.borrower:
                book.borrower[book.isbn.index(int(self.selected[0]))] = "-"
                tkinter.messagebox.showinfo("Info", "You helped %s return this book successfully." % managed_user)
                self.load_data()
                book.save()
            elif self.user in book.borrower:
                book.borrower[book.isbn.index(int(self.selected[0]))] = "-"
                tkinter.messagebox.showinfo("Info", "You successfully return this book.")
                self.load_data()
                book.save()
            else:
                tkinter.messagebox.showinfo("Info", "Unable to find this user (%s) on the borrowed list."
                                            % managed_user)
        else:
            book.borrower[book.isbn.index(int(self.selected[0]))] = "-"
            tkinter.messagebox.showinfo("Info", "You successfully return this book.")
            self.load_data()
            book.save()

    @staticmethod
    def sign_in():
        def sign_validate(user, password):
            success = data.validate_login(user, password)
            if not success:
                tkinter.messagebox.showinfo("Login failed!", "Wrong user name or password.\nPlease try again!")
                login.focus_set()
            else:
                tkinter.messagebox.showinfo("Info", "Sign in success!")
                main.user = user
                main.user_level = success[1]
                main.load_data()
                main.menu_bar.entryconfig("Sign in", state=DISABLED)
                main.menu_bar.entryconfig("Sign out", state=NORMAL)
                if success[1] == 10:
                    main.add_book_button.configure(state=NORMAL)
                    main.remove_book_button.configure(state=NORMAL)
                    main.search_button.configure(state=NORMAL)
                    # main.Button4.configure(state=NORMAL)
                    main.borrow_button.configure(state=NORMAL)
                    main.return_button.configure(state=NORMAL)
                    main.managed_user.configure(state=NORMAL)
                    main.search_entry.configure(state=NORMAL)
                else:
                    main.search_button.configure(state=NORMAL)
                    # main.Button4.configure(state=NORMAL)
                    main.borrow_button.configure(state=NORMAL)
                    main.return_button.configure(state=NORMAL)
                    main.search_entry.configure(state=NORMAL)
                login.destroy()

        login = Toplevel(root)
        font1 = "-family {Segoe UI} -size 11 -weight normal -slant roman -underline 0 -overstrike 0"
        font2 = "-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"
        font3 = "-family {Segoe UI} -size 11 -weight bold -slant roman -underline 1 -overstrike 0"

        login.geometry("320x200+350+200")
        login.title("User Authentication")
        login.configure(background="#BBDEFB")

        label1 = Label(login)
        label1.place(relx=0.08, rely=0.15, height=40, width=92)
        label1.configure(background="#BBDEFB")
        label1.configure(disabledforeground="#a3a3a3")
        label1.configure(font=font3)
        label1.configure(foreground="#212121")
        label1.configure(text='''Username:''')
        label1.configure(width=96)

        e1 = Entry(login)
        e1.place(relx=0.38, rely=0.15, height=35, relwidth=0.51)
        e1.configure(background="white")
        e1.configure(disabledforeground="#a3a3a3")
        e1.configure(font="TkFixedFont")
        e1.configure(foreground="#212121")
        e1.configure(insertbackground="black")
        e1.configure(width=184)

        l2 = Label(login)
        l2.place(relx=0.08, rely=0.36, height=40, width=96)
        l2.configure(background="#BBDEFB")
        l2.configure(disabledforeground="#a3a3a3")
        l2.configure(font=font3)
        l2.configure(foreground="#212121")
        l2.configure(text='''Password:''')
        l2.configure(width=96)

        e2 = Entry(login)
        e2.place(relx=0.38, rely=0.37, height=35, relwidth=0.51)
        e2.configure(background="white")
        e2.configure(disabledforeground="#a3a3a3")
        e2.configure(font="TkFixedFont")
        e2.configure(foreground="#212121")
        e2.configure(insertbackground="black")
        e2.configure(width=184)
        e2.configure(show='*')

        signin_button = Button(login)
        signin_button.place(relx=0.16, rely=0.63, height=53, width=97)
        signin_button.configure(activebackground="#BBDEFB")
        signin_button.configure(activeforeground="#212121")
        signin_button.configure(background="#BBDEFB")
        signin_button.configure(cursor="fleur")
        signin_button.configure(disabledforeground="#a3a3a3")
        signin_button.configure(font=font2)
        signin_button.configure(foreground="#212121")
        signin_button.configure(highlightbackground="#BBDEFB")
        signin_button.configure(highlightcolor="black")
        signin_button.configure(pady="0")
        signin_button.configure(text='''Sign in''')
        signin_button.configure(width=97)
        signin_button.configure(command=lambda: sign_validate(e1.get(), e2.get()))

        exit_button = Button(login)
        exit_button.place(relx=0.55, rely=0.63, height=53, width=106)
        exit_button.configure(activebackground="#BBDEFB")
        exit_button.configure(activeforeground="#212121")
        exit_button.configure(background="#BBDEFB")
        exit_button.configure(disabledforeground="#a3a3a3")
        exit_button.configure(font=font1)
        exit_button.configure(foreground="#212121")
        exit_button.configure(highlightbackground="#BBDEFB")
        exit_button.configure(highlightcolor="black")
        exit_button.configure(pady="0")
        exit_button.configure(text='''Cancel''')
        exit_button.configure(width=106)
        exit_button.configure(command=lambda: login.destroy())
        login.mainloop()

    @staticmethod
    def register():
        def reg_pass(user, pw, rpw):
            data.load()
            user_list = []
            for i in data.user_data:
                user_list.append(i["username"])
            if pw != rpw:
                tkinter.messagebox.showinfo("Register failed!", "Password and repeat password do not match.\n"
                                                                "Please try again!")
                register.focus_set()
            elif user in user_list:
                tkinter.messagebox.showinfo("Register failed!", "User (%s) has been registered.\n"
                                                                "Please try again!" % user)
                register.focus_set()
            elif user == "":
                tkinter.messagebox.showinfo("Register failed!", "Please enter user name!")
                register.focus_set()
            else:
                pwd = base64.b64encode(data.encrypt_pass(pw)).decode('utf-8')
                level = 1
                if main.user_level == 10:
                    level = 10
                with codecs.open("user_db.json", "a", "utf-8") as f:
                    dic = {"username": user, "pwd": pwd, "level": level}
                    json.dump(dic, f, ensure_ascii=False)
                    f.write('\n')
                data.load()
                if level == 10 and admin.get() == 1:
                    tkinter.messagebox.showinfo("Register success!",
                                                "Administrator (%s) has been successfully registered.\n"
                                                "User database has been updated." % user)
                else:
                    tkinter.messagebox.showinfo("Register Success!",
                                                "User (%s) has been successfully registered.\n"
                                                "User database has been updated." % user)
                register.destroy()

        register = Toplevel(root)
        font1 = "-family {Segoe UI} -size 11 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"
        font2 = "-family {Segoe UI} -size 12 -weight bold -slant " \
                "roman -underline 0 -overstrike 0"
        font3 = "-family {Segoe UI} -size 10 -weight bold -slant " \
                "roman -underline 1 -overstrike 0"

        register.geometry("320x220+350+200")
        register.title("User Authentication")
        register.configure(background="#BBDEFB")

        username_label = Label(register)
        username_label.place(relx=0.06, rely=0.06, height=30, width=92)
        username_label.configure(background="#BBDEFB")
        username_label.configure(disabledforeground="#a3a3a3")
        username_label.configure(font=font3)
        username_label.configure(foreground="#212121")
        username_label.configure(text='''Username:''')
        username_label.configure(width=96)

        e1 = Entry(register)
        e1.place(relx=0.45, rely=0.06, height=30, relwidth=0.40)
        e1.configure(background="white")
        e1.configure(disabledforeground="#a3a3a3")
        e1.configure(font="TkFixedFont")
        e1.configure(foreground="#212121")
        e1.configure(insertbackground="black")
        e1.configure(width=184)

        passwd_label = Label(register)
        passwd_label.place(relx=0.06, rely=0.22, height=30, width=96)
        passwd_label.configure(background="#BBDEFB")
        passwd_label.configure(disabledforeground="#a3a3a3")
        passwd_label.configure(font=font3)
        passwd_label.configure(foreground="#212121")
        passwd_label.configure(text='''Password:''')
        passwd_label.configure(width=96)

        e2 = Entry(register)
        e2.place(relx=0.45, rely=0.22, height=30, relwidth=0.40)
        e2.configure(background="white")
        e2.configure(disabledforeground="#a3a3a3")
        e2.configure(font="TkFixedFont")
        e2.configure(foreground="#212121")
        e2.configure(insertbackground="black")
        e2.configure(width=184)
        e2.configure(show='*')

        label3 = Label(register)
        label3.place(relx=0.06, rely=0.39, height=30, width=120)
        label3.configure(background="#BBDEFB")
        label3.configure(disabledforeground="#a3a3a3")
        label3.configure(font=font3)
        label3.configure(foreground="#212121")
        label3.configure(text='''Repeat Password:''')
        label3.configure(width=96)

        entry3 = Entry(register)
        entry3.place(relx=0.45, rely=0.39, height=30, relwidth=0.40)
        entry3.configure(background="white")
        entry3.configure(disabledforeground="#a3a3a3")
        entry3.configure(font="TkFixedFont")
        entry3.configure(foreground="#212121")
        entry3.configure(insertbackground="black")
        entry3.configure(width=184)
        entry3.configure(show='*')

        admin = IntVar()
        checkbutton1 = Checkbutton(register)
        checkbutton1.place(relx=0.06, rely=0.55, relheight=0.14, relwidth=0.40)
        checkbutton1.configure(background="#BBDEFB", disabledforeground="#a3a3a3", foreground="#212121")
        checkbutton1.configure(activebackground="#BBDEFB")
        checkbutton1.configure(activeforeground="#212121")
        checkbutton1.configure(justify=LEFT, text='''As administrator''', variable=admin)
        if main.user_level == 10:
            checkbutton1.configure(state=NORMAL)
        else:
            checkbutton1.configure(state=DISABLED)

        reg_button = Button(register)
        reg_button.place(relx=0.30, rely=0.70, height=45, width=80)
        reg_button.configure(activebackground="#BBDEFB")
        reg_button.configure(activeforeground="#212121")
        reg_button.configure(background="#BBDEFB")
        reg_button.configure(cursor="fleur")
        reg_button.configure(disabledforeground="#a3a3a3")
        reg_button.configure(font=font2)
        reg_button.configure(foreground="#212121")
        reg_button.configure(highlightbackground="#BBDEFB")
        reg_button.configure(highlightcolor="black")
        reg_button.configure(pady="0")
        reg_button.configure(text='''Register''')
        reg_button.configure(width=97)
        reg_button.configure(command=lambda: reg_pass(e1.get(), e2.get(), entry3.get()))

        exit_button = Button(register)
        exit_button.place(relx=0.60, rely=0.70, height=45, width=80)
        exit_button.configure(activebackground="#BBDEFB")
        exit_button.configure(activeforeground="#212121")
        exit_button.configure(background="#BBDEFB")
        exit_button.configure(disabledforeground="#a3a3a3")
        exit_button.configure(font=font1)
        exit_button.configure(foreground="#212121")
        exit_button.configure(highlightbackground="#BBDEFB")
        exit_button.configure(highlightcolor="black")
        exit_button.configure(pady="0")
        exit_button.configure(text='''Cancel''')
        exit_button.configure(width=106)
        exit_button.configure(command=lambda: register.destroy())
        register.mainloop()

    def sign_out(self):
        self.menu_bar.entryconfig("Sign in", state=NORMAL)
        self.add_book_button.configure(state=DISABLED)
        self.remove_book_button.configure(state=DISABLED)
        self.search_button.configure(state=DISABLED)
        self.borrow_button.configure(state=DISABLED)
        self.return_button.configure(state=DISABLED)
        self.search_entry.delete(0, 'end')
        self.search_entry.configure(state=DISABLED)
        self.managed_user.delete(0, 'end')
        self.managed_user.configure(state=DISABLED)
        self.notice_label.configure(text="Please Sign in!")
        self.tree_view.delete(*self.tree_view.get_children())
        self.user = ""
        self.user_level = 0
        self.menu_bar.entryconfig("Sign out", state=DISABLED)
        tkinter.messagebox.showinfo("INFO", "Success sign out!\nData saved.")
        book.save()


if __name__ == "__main__":
    data = Database()  # load init user data and book data
    book = Book(data.book_data)  # load book data
    # for test
    """pwd = data.encrypt_pass("jtc123456")
    print(data.check_pwd(pwd, 'jtc123456'))
    print(data.user_data)
    print(data.book_data)
    print(base64.b64encode(pwd))"""

    root = Tk()  # load root tkinter framework
    main = Library(root)
    # main.load_data()
    root.mainloop()  # main thread
