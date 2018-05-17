#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - Error_Handling.py
# Created by JT on 16/05/2018 14:29.
# Blog: https://blog.jtcat.com/
#
__author__ = 'JT <jiting@jtcat.com>'
'''part 1
q1) Read in numbers and then round to integers
q2) Read in a ten character string, and print out each character on a new line
q3) Read two numbers, and print the result of dividing the first number by the second (watch out for zeros!)
'''


def q1(h=1, i=""):
    try:
        f1 = float(x_input(1, h, i))
        return round(f1)
    except ValueError as e:
        print('except: wrong input,', e)


def q2(h=1, i=""):
    try:
        s1 = str(x_input(2, h, i))
        if len(s1) != 10:
            raise IndexError
        for i in range(0, 10):
            print(s1[i])
    except IndexError as e:
        print('except: wrong input, the string is less or more than ten character.', e)
    return "finish q2"


def q3(h=1, i=""):
    try:
        if h == 0:
            data = i.split()
            n1 = float(data[0])
            n2 = float(data[1])
        else:
            n1 = float(x_input(3, h, i))
            n2 = float(x_input(3, h, i))
        r = n1 / n2
        print("Dividing the first number by the second...")
        print('result:', r)
    except ZeroDivisionError as e1:
        print('except:', e1)
    except ValueError as e2:
        print('except: wrong input,', e2)
    return "finish q3"


'''part 2
In this section, we’ll define functions that throw exceptions to handle unusual situations. In each case throw an 
appropriate exception for the problem rather than using the default exception.

q4)	Define a function that converts a string to lowercase, but that throws an exception if there are no uppercase 
    characters in the string.
q5)	Define a function that prints out all the items of a list, but throws an exception if the list is empty.
q6)	Define a function that takes a tuple of length of three as an argument and prints out the elements in reverse 
    order, but throws an exception if the tuple does not have exactly three elements.
'''


def q4(h=1, i=""):
    try:
        str1 = x_input(4, h, i)
        count = 0
        for i in list(str1):
            if i.isupper():
                count += 1
        if count == 0:
            raise ValueError("No uppercase characters in the string!")
        return str1.lower()
    except ValueError as e:
        print('except:', e)


def q5(h=1, i=""):
    try:
        list1 = x_input(5, h, i).split()
        # list1 = ["abc", 0, "DEF"]
        # set list1 to empty
        # list1 = []
        if not list1:
            raise Exception
        for i in list1:
            print(i)
    except Exception as e:
        print(e)
    return "finish q5"


def q6(h=1, i=""):
    try:
        tuple1 = (x_input(6, h, i).split())
        if len(tuple1) != 3:
            raise Exception(IndexError("the tuple does not have exactly three elements"))
        for i in range(3):
            print(tuple1[int(-i)])
    except Exception as e:
        print(e)
    return "finish q6"


def x_input(x, y, z):
    if x == 1:
        if y == 0:
            x1 = z
            return x1
        print("Enter a number: ", end="")
        x1 = input()
        return x1
    if x == 2:
        if y == 0:
            x2 = z
            return x2
        print("Enter a string has more than ten character: ", end="")
        x2 = input()
        return x2
    if x == 3:
        if y == 1:
            print("Enter the first number:", end="")
            x3 = input()
            return x3
        elif y == 2:
            print("Enter the second number:", end="")
            x3 = input()
            return x3
    if x == 4:
        if y == 0:
            x4 = z
            return x4
        print("Enter a string with uppercase then I will convert it to lowercase: ", end="")
        x4 = input()
        return x4
    if x == 5:
        if y == 0:
            x5 = z
            return x5
        print("Enter something and separate with spaces :)\n", end="")
        x5 = input()
        return x5
    if x == 6:
        if y == 0:
            x6 = z
            return x6
        print("Enter something and separate with spaces :)\n", end="")
        x6 = input()
        return x6


'''part 3
Let’s combine Parts 1 and 2. Write a simple line interface to the functions from Part 2 that allows a user to 
select the functions and enter the appropriate input. The interface should check that the user’s input is valid 
before calling the requested function.
'''


def check(i):
    if i == 1:
        print("\nChecking question 1:")
        print("\nwith data 42:")
        print(q1(0, "42"))
        print("\nwith data 42.01:")
        print(q1(0, "42.01"))
        print("\nwith data 42.quq:")
        print(q1(0, "42.quq"))
    elif i == 2:
        print("\nChecking question 2:")
        print("\nwith data 'qwertyuiop':")
        print(q2(0, "qwertyuiop"))
        print("\nwith data 'qwertyuiop123':")
        print(q2(0, "qwertyuiop123"))
        print("\nwith data 'qw123':")
        print(q2(0, "qw123"))
    elif i == 3:
        print("\nChecking question 3:")
        print("\nwith data '100 20':")
        print(q3(0, "100 20"))
        print("\nwith data '30 0':")
        print(q3(0, "30 0"))
        print("\nwith data 'quq 0':")
        print(q3(0, "quq 0"))
    elif i == 4:
        print("\nChecking question 4:")
        print("\nwith data 'QwErTy':")
        print(q4(0, "QwErTy"))
        print("\nwith data 'QwErTy123':")
        print(q4(0, "QwErTy123"))
        print("\nwith data 'qwer123':")
        print(q4(0, "qwer123"))
    elif i == 5:
        print("\nChecking question 5:")
        print("\nwith data '[\"abc\", 0, \"DEF\"]':")
        print(q5(0, "abc 0 DEF"))
        print("\nwith empty data '':")
        print(q5(0, ""))
        print("\nwith data 'none':")
        print(q5(0, "0"))
    elif i == 6:
        print("\nChecking question 6:")
        print("\nwith data 'qwe rty uiop':")
        print(q6(0, "qwe rty uiop"))
        print("\nwith data 'qwe rty uiop 123':")
        print(q6(0, "qwe rty uiop 123"))
        print("\nwith data 'qw 123':")
        print(q6(0, "qw 123"))


def auto_check(x):
    print("\nAuto Check with test data.")
    if x == 0:
        for i in range(1, 7):
            check(i)
    elif 1 <= x <= 6:
        check(x)
    else:
        print("Wrong parameter")


def main():
    while True:
        print("\nError Handling Simple Line Interface :)\n By:", __author__)
        print("Do function auto check?(y/n)", end="")
        if input() == "y":
            print("Which function do you want to check?(1-6,all)", end="")
            operate = input()
            if operate == "all":
                auto_check(0)
            elif operate.isdigit():
                auto_check(int(operate))
        print("Now Manual selection function: (4,5,6)", end="")
        operate = input()
        if operate == "4":
            count = 0
            x4 = 0
            while count == 0:
                print("Enter a string with uppercase then I will convert it to lowercase: ", end="")
                x4 = input()
                for i in list(x4):
                    if i.isupper():
                        count += 1
                if count == 0:
                    print("Wrong input! Please try again!")
            print(q4(0, x4))
            print("\nContinue or exit?", end="")
            if not input():
                break
        elif operate == "5":
            count = 0
            while count == 0:
                print("Enter something and separate with spaces :)\n", end="")
                x5 = input()
                if x5:
                    print(q4(0, x5))
                    count += 1
                else:
                    print("Wrong input! Please try again!")
            print("\nContinue or exit?", end="")
            if not input():
                break
        elif operate == "6":
            count = 0
            while count == 0:
                print("Enter three whatever (as elements) and separate with spaces :)\n", end="")
                x6 = input()
                tuple1 = (x6.split())
                if len(tuple1) == 3:
                    print(q6(0, x6))
                    count += 1
                else:
                    print("Wrong input! Please try again!")
            print("\nContinue or exit?", end="")
            if not input():
                break


if __name__ == '__main__':
    main()
