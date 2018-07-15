#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - q3.py
# Created by JT on 25-Jun-18 11:56.

data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
tmp = []
for i in data:
    for j in i:
        tmp.append(i[j])
output = set(tmp)
print(output)
