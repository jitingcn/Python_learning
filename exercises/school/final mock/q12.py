#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - q12.py
# Created by JT on 15-Jul-18 00:28.

from tkinter import *

units = {"mm": 10, "inches": 0.393701}

top = Tk()
top.geometry("300x90+400+300")
var1 = StringVar(top)
var1.set("mm")
Label(top, text="Amount:").grid(row=0)
amount = Entry(top)
amount.grid(row=0, column=1)
Label(top, text=" centimetres").grid(row=0, column=2)
Label(top, text="Convert to:").grid(row=1)
option = OptionMenu(top, var1, "mm", "inches")
option.grid(row=1, column=1)
Button(top, text="Convert", command=lambda: convert()).grid(row=1, column=2)
output = Label(top, text=" ")
output.grid(row=2, column=1)


def convert():
    a = int(amount.get())
    o = units[var1.get()]
    out = a * o
    output.configure(text="%s cm = %.2f %s" % (a, out, var1.get()))


top.mainloop()
