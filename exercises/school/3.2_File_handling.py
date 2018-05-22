#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - 3.2_File_handling.py
# Created by JT on 21/05/2018 22:15.
# Blog: https://blog.jtcat.com/
#
import os
import json
# Part 1 – Reading birthdays from a file

# def getBirthdays(fileName, book):
# According to Python coding style guide (https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)
# Both function and argument name should be lowercase. Separate function name should use underline, not capital.


def get_birthdays(filename, book=None):
    if book is None:
        book = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            tmp = line.strip().split(",")
            book[tmp[0]] = {"month": tmp[1], "day": int(tmp[2])}
    return book

# Part 2 – A complete birthday book application


def name_birth(birth, name):
    try:
        if name in birth:
            print(name + "'s birthday is", birth[name]["day"], birth[name]["month"])
        else:
            raise IndexError
    except IndexError:
        print("Can't find", name)


def month_birth(birth, month):  # TODO
    try:
        for i in birth:
            if month == birth[i]["month"]:
                print()
    except IndexError:
        print()


def next_birth():  # TODO
    pass


def test_data(method, birth=None):  # create and delete test data
    if birth is None:
        birth = {}
    if method == 0:  # create test data
        with open("test.txt", 'w', encoding="utf-8") as f:
            f.write("John,Mar,23\n"
                    "Susan,Feb,16\n"
                    "Duncan,May,20\n"
                    "Holland,Jan,3\n"
                    "Stephenson,Feb,14\n"
                    )
    elif method == 1:  # delete test data
        os.remove("test.txt")
    elif method == 2:  # save birthday book
        with open("birth.json", 'a', encoding="utf-8") as f:
            f.write(json.dumps(birth))
    elif method == 3:  # delete birthday book
        os.remove("birth.json")


def main():  # TODO
    print("Birthday book by Jiting")
    test_data(0)
    data = get_birthdays("test.txt")
    print(data)
    name_birth(data, "Susan")
    test_data(2, data)
    test_data(3)
    test_data(1)


if __name__ == '__main__':
    main()
