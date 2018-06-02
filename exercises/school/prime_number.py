#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import timeit
from itertools import compress


def prime(n):
    flag = [1]*(n+2)
    p = 2
    primes_l = []
    while p <= n:
        primes_l.append(p)
        for i in range(2*p, n+1, p):
            flag[i] = 0
        while 1:
            p += 1
            if flag[p] == 1:
                break
    return primes_l


def rwh_primes1v1(n):  # https://stackoverflow.com/a/46635266
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


def rwh_primes1v2(n):  # https://stackoverflow.com/a/46635266
    """ Returns a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1, int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


def main(c=3, r=1000000, s=0):
    print("\nPrime Number in %d: " % r)
    len_list = []
    start = timeit.default_timer()
    for b in range(c):
        len_list = rwh_primes1v2(r)
    elapsed = (timeit.default_timer() - start) / c
    print("length:", len(len_list))
    print(c, "calculations average time: %.6f s" % elapsed)
    if s == 0:
        print("Max prime: %d\n" % len_list[-1])
    elif s == 1:
        print(len_list)


if __name__ == '__main__':
    try:
        if os.name == "posix":
            if len(sys.argv) < 2:
                print("Usage: ./prime_number.py times ranges show_list(0/1)")
                print("Example: ./prime_number.py 3 1000000")
            else:
                times = int(sys.argv[1])
                ranges = int(sys.argv[2])
                if not sys.argv[3]:
                    show_list = 0
                else:
                    show_list = int(sys.argv[3])
                main(times, ranges, show_list)
        else:
            main(int(input("Enter test times: ")),
                 int(input("Enter test range:")),
                 int(input("Show list? (0=no 1=yes): ")))
    except Exception as e:
        print(e)
