#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - 3.2_File_handling.py
# Created by JT on 21/05/2018 22:15.
# Blog: https://blog.jtcat.com/
#
import os
import json
# Part 1 – Reading birthdays from a file

# Questions asked: def getBirthdays(fileName, book):
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


def date_check(book):
    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    long_month = ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]
    short_month = ["Feb", "Apr", "Jun", "Sep", "Nov"]
    remove_set = set()
    print("\nSimple check of dates")
    for i in book:
        if book[i]["month"] not in month:
            print(i + ":", book[i]["day"], book[i]["month"])
            print("The month of", i + "'s birthday seen not right. Please make sure there are no misspellings.")
            print("Prepare remove", i, "from birthday book")
            remove_set.add(i)
        if book[i]["month"] in long_month:
            if not 1 < book[i]["day"] < 31:
                print(i + ":", book[i]["day"], book[i]["month"])
                print("The day of", i + "'s birthday seen not right. Please make sure there are no misspellings.")
                print("Prepare remove", i, "from birthday book")
                remove_set.add(i)
        if book[i]["month"] in short_month:
            if not 1 < book[i]["day"] < 30:
                print(i + ":", book[i]["day"], book[i]["month"])
                print("The day of", i + "'s birthday seen not right. Please make sure there are no misspellings.")
                print("Prepare remove", i, "from birthday book")
                remove_set.add(i)
    for i in remove_set:
        del book[i]
    return book


def name_birth(book, name):
    try:
        if name in book:
            print("\n" + name + "'s birthday is", book[name]["day"], book[name]["month"])
        else:
            raise IndexError
    except IndexError:
        print("Can't find", name)


def month_birth(book, month):
    count = 0
    try:
        print("\nChecking birthday")
        for i in book:
            if month == book[i]["month"]:
                print(i + ":", book[i]["day"], month)
                count += 1
        print(count, "people's birthday in", month)
    except IndexError:
        print()


def next_birth(book, month, day):  # TODO
    count = 0
    try:
        print("\nThese people's birthdays within a week after", day, month)
        for i in book:
            if month == book[i]["month"]:
                print(i + ":", book[i]["day"], month)
                count += 1
        print(count, "people's birthday in", month)
    except IndexError:
        print()


def test_data(method, book=None):  # create and delete test data
    if book is None:
        book = {}
    if method == 0:  # create test data
        with open("test.txt", 'w', encoding="utf-8") as f:
            f.write("John,Mar,23\n"
                    "Susan,Feb,16\n"
                    "Duncan,May,20\n"
                    "Holland,Jan,3\n"
                    "Stephenson,Feb,14\n"
                    "Stephen,Jan,32\n"
                    )
    elif method == 1:  # delete test data
        os.remove("test.txt")
    elif method == 2:  # save birthday book
        with open("birth.json", 'a', encoding="utf-8") as f:
            f.write(json.dumps(book))
    elif method == 3:  # delete birthday book
        os.remove("birth.json")


def main():  # TODO
    print("Birthday book by Jiting (testing)")
    test_data(0)
    data = get_birthdays("test.txt")
    data = date_check(data)
    # print(data)
    name_birth(data, "Susan")
    month_birth(data, "Mar")
    # next_birth(data, "Mar", 20)
    test_data(2, data)
    test_data(3)
    test_data(1)


if __name__ == '__main__':
    main()
