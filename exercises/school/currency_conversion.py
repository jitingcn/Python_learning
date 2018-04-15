#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - currency_conversion.py
# Created by JT on 4/15/2018 17:57.
# Blog: https://blog.jtcat.com/

# 4.Currency Conversion
# The program should let the user convert between two currencies from the list of currencies below.
# The conversion rates between each currency and GBP (£) are given, however the program should be able to
# convert between any two currencies on the list. The user should be able to input an amount
# in currency A and the program should give the value of the inputted amount in currency B.
# The currencies and their exchange rates with GBP (£) are
# •	Great British Pound - GBP 1:1
# •	United States Dollar - USD 1:1.30
# •	EUR 1:1.15
# •	Japanese YEN 1:150
# •	Australian Dollar - AUD 1:1.75
# •	Chinese Yuan - CHY 1:8.80

__author__ = 'JT <jiting@jtcat.com>'

rates = {"GBP": 1, "USD": 1.3, "EUR": 1.15, "YEN": 150, "AUD": 1.75, "CNY": 8.80}


def exchange_rate(o, t):
    origin = rates.get(o)
    target = rates.get(t)
    rate = target / origin
    return rate


def main():
    print("Welcome to Currency Converter")
    print("Supported currency: GBP USD EUR YEN AUD CNY")
    print("Enter the origin currency that you wish to convert: ", end="")
    origin = input().upper()
    print("Enter the target currency that you wish to convert: ", end="")
    target = input().upper()
    rate = exchange_rate(origin, target)
    amount = float(input("Enter the amount you wish to convert: "))
    target_amount = amount * rate
    print(amount, origin, "=", target_amount, target)


if __name__ == '__main__':
    main()
