#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

union = set(a) | set(b)
intersection = union - set(a) ^ set(b)
diff_a = set(a) - set(intersection)
diff_b = set(b) - set(intersection)

print("difference:")
print("a: ", diff_a, "b: ", diff_b)
