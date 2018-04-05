#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - decode_QQ_whoSaid.py
# Created by JT on 4/5/2018 03:55.
# Blog: https://blog.jtcat.com/

# reference: https://www.zhaoj.in/read-4821.html
__author__ = 'JT <jiting@jtcat.com>'
__version__ = "0.2 Alpha"

import json

data = """

"""
data = json.loads(data)


def get_user(text):
    keys = {"oe": "0", "n": "0", "z": "0", "on": "0",
            "oK": "1", "6": "1", "5": "1",
            "ow": "2", "-": "2", "A": "2", "oc": "2",
            "oi": "3", "i": "3", "o": "3", "oz": "3",
            "7e": "4", "v": "4", "P": "4", "7n": "4",
            "7K": "5", "4": "5", "k": "5", "7": "5", "7v": "5",
            "7w": "6", "C": "6", "s": "6", "7c": "6",
            "7i": "7", "S": "7", "l": "7", "7z": "7",
            "Ne": "8", "c": "8", "F": "8", "Nn": "8", "ov": "8",
            "NK": "9", "E": "9", "q": "9", "Nv": "9",
            }

    # text = ""
    final_string = ""

    text = text.replace("*S1*", "")

    while text:
        if len(text) > 1:
            if not keys.__contains__(text[:2]):
                current_value = keys.get(text[:1])
                text = text[1:]
            else:
                current_value = keys.get(text[:2])
                text = text[2:]
            final_string = final_string + str(current_value)
        else:
            final_string = final_string + str(keys.get(text))
            text = ""
    return final_string


for i in data["data"]["confesses"]:
    print(get_user(i["fromEncodeUin"]))

get_user("")
