#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - QQHonestSayDecode.py
# Created by JT on 4/5/2018 03:55.
# Blog: https://blog.jtcat.com/

# reference: https://www.zhaoj.in/read-4821.html
# Put captured json data into data.json in the directory first!
__author__ = 'JT <jiting@jtcat.com>'
__version__ = "0.9 Beta"

import json
from datetime import datetime, timedelta, timezone


class Main(object):

    def __init__(self):
        self.dict = {"oe": "0", "n": "0", "z": "0", "on": "0",
                     "oK": "1", "6": "1", "5": "1",
                     "ow": "2", "-": "2", "A": "2", "oc": "2",
                     "oi": "3", "i": "3", "o": "3", "oz": "3", "w": "3",
                     "7e": "4", "v": "4", "P": "4", "7n": "4",
                     "7K": "5", "4": "5", "k": "5", "7": "5", "7v": "5",
                     "7w": "6", "C": "6", "s": "6", "7c": "6",
                     "7i": "7", "S": "7", "l": "7", "7z": "7",
                     "Ne": "8", "c": "8", "F": "8", "Nn": "8", "ov": "8",
                     "NK": "9", "E": "9", "q": "9", "Nv": "9",
                     }
        with open("data.json", "rb") as f:
            raw = json.load(f)
        self.data = raw["data"]["confesses"]

    def decode(self, data):
        result = ""
        string = data.replace("*S1*", "")

        while string:
            if len(string) > 1:
                if self.dict.__contains__(string[:2]):
                    current_value = self.dict.get(string[:2])
                    string = string[2:]
                elif self.dict.__contains__(string[:1]):
                    current_value = self.dict.get(string[:1])
                    string = string[1:]
                else:
                    current_value = ""
                    string = string[1:]
                result += str(current_value)
            else:
                result += str(self.dict.get(string))
                string = ""
        return result

    def start(self):
        for i in self.data:
            if i["fromGender"] == "0":
                gender = "Male"
            else:
                gender = "Female"
            description = i["fromNick"]
            account = self.decode(i["fromEncodeUin"])
            receiver = i["toNick"]
            topic = i["topicName"]
            timestamp = datetime.utcfromtimestamp((i["timestamp"])).astimezone(timezone(timedelta(hours=8)))
            print(description, "账号:", account, "认为", receiver, topic, "在", timestamp)


if __name__ == "__main__":
    Main().start()
