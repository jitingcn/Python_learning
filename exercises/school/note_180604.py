#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - note_180604.py
# Created by JT on 04/06/2018 09:57.

"""
Read numbers from a file
check prime
save to a file
"""
import json
from itertools import compress


def rwh_primes1v2(n):  # https://stackoverflow.com/a/46635266
    """ Returns a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1, int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


def get_numbers(filename, nums=None):
    print("\nLoading data...")
    if nums is None:
        nums = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            tmp = line.strip()
            try:
                tmp = int(tmp)
                nums[tmp] = False
            except ValueError as e:
                print(tmp + ": Not a valid input", "\nSkip...")
            # print(nums)
    # nums = sorted(nums.keys())
    # nums = num_check(nums)
    print("Input: ", nums)
    return nums


def check_prime(nums):
    n_max = int(max(nums, key=int))
    prime_list = rwh_primes1v2(n_max)
    for i in dict.keys(nums):
        if i in prime_list:
            nums[i] = True
    return nums


def save_primes(nums):
    with open("prime.txt", 'w', encoding="utf-8") as f:
        f.write(json.dumps(nums))


def main():
    try:
        filename = input("Enter the file name: ")
        primes = check_prime(get_numbers(filename))
        print("Output: ", primes)
        save_primes(primes)
        print("DONE")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
