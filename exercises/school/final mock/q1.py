#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections


def init_file():
    # create data file
    with open("q1.txt", "w") as q1f:
        q1f.write("""'Simple', 'NN'
'is', 'VBZ'
'better', 'JJR'
'than', 'IN'
'complex', 'JJ'
------------------------
'Nice', 'JJ'
'place', 'NN'
'Better', 'NNP'
'than', 'IN'
'some', 'DT'
'reviews','NNS'
'give', 'VBP'
'it', 'PRP'
'credit, 'NN'
'for', 'IN'
------------------------""")


def read():
    # read from file
    data = []
    with open("q1.txt", "r") as q1f:
        for i in q1f.readlines():
            line = i.strip().replace("'", "").replace(" ", "").split(",")
            if len(line) == 2:
                data.append(line[1])
    data = dict(collections.Counter(data))
    return data


init_file()
print(read())
# TODO: see below
'''
    Thereafter the program should allow the user to enter in more sentences, one at a time, 
    the program should write these sentences to file, one word per line.
    Please use at least once instance of exception handling.
'''
