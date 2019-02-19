#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1008
# 2019/2/19 Jiting
"""

"""
m = input().split(" ")
length = int(m[0])
move = int(m[1])
data = input().split(" ")
data_left = data[length-move:]
data_right = data[:length-move]
data = data_left + data_right
print(" ".join(data))