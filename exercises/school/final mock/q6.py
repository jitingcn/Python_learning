#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

a = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
b = [1, 2, 2, 3]
s = zip(a, b)
d = collections.defaultdict(set)
for i, j in s:
    d[i].add(j)

print(d)
