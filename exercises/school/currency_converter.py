#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - currency_converter.py
# Created by JT on 11/06/2018 09:56.

from tkinter import *
from tkinter import ttk


class Converter(Frame):
    rates = {"GBP": 1, "USD": 1.3, "EUR": 1.15, "YEN": 150, "AUD": 1.75, "CNY": 8.80}

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.o_amount = Entry(master).grid(column=0, row=0)
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.origin_currency = OptionMenu(master, self.var1, "GBP", "USD", "EUR", "YEN", "AUD", "CNY")
        self.origin_currency.grid(column=0, row=1)
        self.target_currency = OptionMenu(master, self.var2, "GBP", "USD", "EUR", "YEN", "AUD", "CNY")
        self.target_currency.grid(column=0, row=2)
        self.button = Button(master, text='convert', command=self.convert)
        self.button.grid(column=0, row=4)
        self.t_amount = Label(master)
        self.t_amount.grid(column=0, row=3)
        self.grid()

    def convert(self):
        amount = float(self.o_amount.get()) or 0
        origin_currency = self.var1.get() or "GBP"
        target_currency = self.var2.get() or "CNY"
        target_amount = amount * self.exchange_rate(origin_currency, target_currency)
        self.t_amount.configure(text=target_amount)

    def exchange_rate(self, o, t):
        origin = self.rates.get(o)
        target = self.rates.get(t)
        rate = target / origin
        return rate


app = Converter()
app.master.title('Currency Converter')
app.mainloop()
