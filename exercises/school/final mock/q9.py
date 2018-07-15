#!/usr/bin/env python
# -*- coding: utf-8 -*-


def search(list1, n):
    if len(list1) == 0:
        return False
    elif n == list1[0]:
        return True
    else:
        return search(list1[1:], n)


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert search(li, 41) is False
assert search(li, 10) is True
