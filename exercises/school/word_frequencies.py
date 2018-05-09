#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - word_frequencies.py
# Created by JT on 09/05/2018 09:36.
# Blog: https://blog.jtcat.com/
# 
__author__ = 'JT <jiting@jtcat.com>'
import re
import collections


def word_freq(words):
    # words = input("Please give a string for statistics word frequency.")
    temp = re.sub('[+.!_,$%^*(\"\')]', "", words).lower().strip("").split()
    return collections.Counter(temp)


print(word_freq("The first test of the function."))
