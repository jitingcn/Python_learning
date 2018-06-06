#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - collatz_conjecture.py
# Created by JT on 06/06/2018 14:18.


def collatz(n, length=None):
    nl = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        elif n % 2 == 1:
            n = n * 3 + 1
        nl.append(n)
    if length:
        length = len(nl) - 1
        return length
    else:
        return nl


def save_list(li, filename=None):
    if not filename:
        filename = "longest_sequence.txt"
    with open(filename, 'w', encoding="utf-8") as f:
        f.write("Largest sequence has starting number %d. The sequence is as follows:\n" % li[0])
        for i in li:
            f.write("%s\n" % i)
    return filename


def max_list(n_max, debug=None):
    maximum_value = 1
    maximum_length = 1
    for i in range(1, n_max+1):
        length = collatz(i, 1)
        if length > maximum_length:
            maximum_value = i
            maximum_length = length
        if debug:
            print("longest: %s | %s: length: %s" % (maximum_value, i, length))
    return maximum_value


def main(n):
    task1_result = collatz(n)
    task1 = map(str, task1_result)
    task1_output = " -> ".join(task1)
    print("\nTasks a: start with %s: \n length=%s\n list=%s" % (n, len(task1_result)-1, task1_output))
    print("\nTask b: find the number less than one million which has the longest Collatz sequence:")
    print("Calculating, please wait...")
    task2_number = max_list(1000000)
    task2_length = collatz(task2_number, 1)
    print(" The number is %s\n length: %s" % (task2_number, task2_length))
    print("\nSave the Collatz sequence of %s..." % task2_number)
    filename = save_list(collatz(task2_number))
    print("Done. Filename:", filename)


if __name__ == '__main__':
    main(13)
