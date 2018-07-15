#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - note_180613.py
# Created by JT on 13/06/2018 14:33.
# a system for analysing the flight paths of aircraft
from tkinter import *

lax = {"LAX": [30, 0]}
gla = {"GLA": [2, 4]}
wtf = {"sp": [100, 100]}
flight = {"AC1000": ["aLIEz", gla, lax],
          "AC1001": ["aLIEz", lax, gla],
          }


class Windows(object):
    print()
