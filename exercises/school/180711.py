#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - 180711.py
# Created by JT on 11-Jul-18 14:13.
import collections
import string


def even_gen(m, n):
    even = []
    for i in range(m, n+1, 2):
        i = str(i)
        a = 0
        for d in i:
            if int(d) % 2 != 0:
                a = 1
        if a == 0:
            even.append(i)
    return ', '.join(even)


def sum_two(a, b):
    return a + b


def ask_pwd():
    while True:
        pwd = input("Enter your password: ")
        if check_pwd(pwd):
            break
    return pwd


def check_pwd(pwd):
    if len(pwd) < 8:
        print("Length less than 8.")
        return False
    else:
        characters = 0
        numbers = 0
        for i in pwd:
            if i.isalpha():
                characters += 1
            elif i.isdigit():
                numbers += 1
        if characters < 3 and numbers < 3:
            print("Less than 3 characters and 3 numbers.")
            print("Actually found %s characters, %s numbers." % (characters, numbers))
            return False
        elif characters < 3:
            print("Less than 3 characters.")
            print("Actually found %s characters, %s numbers." % (characters, numbers))
            return False
        elif numbers < 3:
            print("Less than 3 numbers.")
            print("Actually found %s characters, %s numbers." % (characters, numbers))
            return False
        else:
            print("Meet the requirements.")
            return True


def word_count(text=None):
    if text is None:
        text = input("Enter some text: ")
    text = participle(text, "", 1).split()
    word = dict(collections.Counter(text))
    for i in word:
        print(i, "occurs", word[i])


def participle(s1=None, s2=None, x=0):
    if s1 is None and s2 is None:
        return ""
    elif s2 is None:
        word = s1
    else:
        word = s1 + " " + s2
    if x == 1:
        word = word.lower()
    del_list = string.punctuation + string.digits
    for i in del_list:
        word = word.replace(i, "")
    return word


def q5(s1, s2):
    s = participle(s1, s2)
    alpha = []
    for i in s:
        if i == " ":
            pass
        else:
            alpha.append(i)
    alpha = list(set(alpha))
    print(" ".join(alpha))


def square(m, n):
    out = []
    for i in range(m, n+1):
        out.append(i*i)
    return out


if __name__ == '__main__':
    print(even_gen(1000, 3000))
    assert 100 == sum_two(20, 80)
    # print(ask_pwd())
    word_count("If I wanted to I could run very, very fast")
    print(participle("first sentence", "second sentence"))
    # should print c e f i n o r s t
    print(square(1, 20))
    q5("first sentence", "second sentence")
