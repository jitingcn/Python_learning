#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - q2.py
# Created by JT on 14-Jul-18 23:46.

d = {"aaa"}


def ask():
    while True:
        i = input("Enter a key:")
        if i in d:
            print("This key is already in dictionary.")
            continue
        else:
            d.add(i)
            break


ask()
print(d)
