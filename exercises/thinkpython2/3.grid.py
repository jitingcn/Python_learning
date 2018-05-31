#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - 3.grid.py
# Created by JT on 31/05/2018 23:38.


def grid(x=2, y=2, s=4):
    for b in range(y):
        for a in range(x):
            print('+', end=" ")
            print("- "*s, end="")
        print('+')
        for a in range(s):
            for c in range(x):
                print("|", end=" ")
                print("  "*s, end="")
            print("|")
    for a in range(x):
        print('+', end=" ")
        print("- " * s, end="")
    print('+')


if __name__ == '__main__':
    grid(2, 2, 4)
