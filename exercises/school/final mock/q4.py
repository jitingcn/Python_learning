#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
list1 = []
dict1 = {}
for i in data:
    for j in i:
        list1.append(i[j])
print(list1)
for i in range(0, len(list1), 2):
    if list1[i] in dict1:
        dict1[list1[i]] += list1[i+1]
    else:
        dict1[list1[i]] = list1[i+1]
print(dict1)
