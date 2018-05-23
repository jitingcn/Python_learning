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
    print("\nLoading data...")
    if book is None:
        book = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            tmp = line.strip().split(",")
            book[tmp[0]] = {"month": tmp[1], "day": int(tmp[2])}
    book = date_check(book)
    return book

# Part 2 – A complete birthday book application


def date_check(book):
    month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_x = {"Jan": 31, "Feb": 29, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30,
               "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31}
    remove_set = set()
    print("\nSimple check of dates")
    for i in book:
        if book[i]["month"] not in month_list:
            print("\nThe month of", i + "'s birthday seen not right. Please make sure there are no misspellings.")
            print(i + ":", book[i]["day"], book[i]["month"])
            print("Prepare remove", i, "from birthday book")
            remove_set.add(i)
        elif not 1 <= book[i]["day"] <= month_x[book[i]["month"]]:
            print("\nThe day of", i + "'s birthday seen not right. Please make sure there are no misspellings.")
            print(i + ":", book[i]["day"], book[i]["month"])
            print("Prepare remove", i, "from birthday book")
            remove_set.add(i)
        if book[i]["month"] == "Feb":
            if book[i]["day"] == 29:
                print("\nThe day of", i + "'s birthday seen not right.")
                print(i + ":", book[i]["day"], book[i]["month"])
                print("Warning: The possibility of a birthday on February 29th is extremely low!")
    for i in remove_set:
        del book[i]
    return book

# search functions


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
        print("Find", count, "person")
    except IndexError:
        print()


def next_birth(book, month, day):
    try:
        month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_x = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30,
                   "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31}
        if month in month_list and month != "Dec":
            next_month = month_list[month_list.index(month) + 1]
        elif month == "Dec":
            next_month = "Jan"
        else:
            raise IndexError
        count = 0
        print("\nThese people's birthdays within a week after", day, month)
        for i in book:
            if day <= month_x[book[i]["month"]] - 7 and month == book[i]["month"]:
                if day <= book[i]["day"] <= day + 7:
                    print(i + ":", book[i]["day"], month)
                    count += 1
            elif day > month_x[book[i]["month"]] - 7 and (month == book[i]["month"] or next_month == book[i]["month"]):
                if day <= book[i]["day"] <= month_x[book[i]["month"]]:
                    print(i + ":", book[i]["day"], month)
                    count += 1
                elif book[i]["day"] <= 7 + day - month_x[book[i]["month"]]:
                    print(i + ":", book[i]["day"], next_month)
                    count += 1
        if count == 0:
            print("Warning: Can't find anyone!")
    except IndexError:
        print()

# test function


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
                    "Alpha,Xan,34\n"
                    "Beta,Nov,31\n"
                    "Canada,Jan,32\n"
                    "Dubai,Feb,29\n"
                    )
    elif method == 1:  # delete test data
        os.remove("test.txt")
    elif method == 2:  # save birthday book
        with open("birth.json", 'w', encoding="utf-8") as f:
            f.write(json.dumps(book))
    elif method == 3:  # delete birthday book
        os.remove("birth.json")


def test():
    print("Birthday book by JT (auto test)")
    test_data(0)
    data = get_birthdays("test.txt")
    data = date_check(data)
    print(data)
    name_birth(data, "Susan")
    month_birth(data, "Mar")
    next_birth(data, "Feb", 10)
    test_data(2, data)
    test_data(3)
    test_data(1)


def main():
    print("Birthday book by JT")
    while True:
        if os.path.isfile("birth.json"):
            with open("birth.json", 'r') as f:
                book = json.load(f)
        else:
            book = {}
        print("\nMenu:\n1. Read birthday data from a file.")
        print("2. Manually enter birthday data.")
        print("3. Search birthday by name.")
        print("4. Search birthday by month.")
        print("5. Search people's birthdays within a week.")
        print("6. Quit.")
        print("Select the operation: ", end="")
        try:
            op = int(input())
            if op == 1:
                filename = input("Enter the file name: ")
                book = get_birthdays(filename, book)
                test_data(2, book)
                print("\nData import completed, automatically saved...")
            elif op == 2:
                name = input("Enter the person name: ")
                month = input("Enter the month of birthday [e.p. Mar]: ")
                day = int(input("Enter the day of birthday [e.p. 3]: "))
                book[name] = {"month": month, "day": day}
                test_data(2, book)
            elif op == 3:
                name = input("Enter the people's name that you want to query: ")
                name_birth(book, name)
            elif op == 4:
                month = input("Enter the people's name that you want to query: ")
                month_birth(book, month)
            elif op == 5:
                month, day = input("Enter a date that you want to query [example: Feb 10]: ").split()
                next_birth(book, month, int(day))
            elif op == 6:
                break
        except Exception as e:
            print(e)


if __name__ == '__main__':
    test_data(0)
    main()
