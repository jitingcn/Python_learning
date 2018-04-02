#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - random_password_generator.py
# Created by JT on 4/1/2018 20:47.
# Blog: https://blog.jtcat.com/

# 1.	Random password generator.
# The password generator should print a random string of characters of a random length
# between six and twelve characters long. The password should be created out of a mixture of
# capital letters, A-Z, lower case letters, a-z, numerals, 0-9 and the symbols !, ?, @, #, &, ;, :.
__author__ = 'JT <jiting@jtcat.com>'

import random
seed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?@#&;:"


def pw(digit=0, time=1):
    for x in range(time):
        tmp = []
        if digit == 0:
            for i in range(random.randint(6, 12)):
                tmp.append(random.choice(seed))
        else:
            for i in range(digit):
                tmp.append(random.choice(seed))

        password = ''.join(tmp)
        print(password)

# pw()
