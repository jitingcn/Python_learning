#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - q10.py
# Created by JT on 26-Jun-18 01:33.

a = [1, 25, 7, 12, 25]


def dup1(li):
    count = 0
    for i in li:
        if li.count(i) > 1:
            return True
        else:
            count += 1
    if count == len(li):
        return False


def dup2(li):
    if len(li) == 1:
        return False
    elif li[0] in li[1:]:
        return True
    else:
        return dup2(li[1:])


print(dup1(a))
print(dup2(a))
