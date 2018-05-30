#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - 180530_note.py
# Created by JT on 30/05/2018 10:11.
import timeit


def even_list(n):  # even number
    evens = []
    for i in range(n+1):
        if not i % 2:
            evens.append(str(i))
    return " ".join(evens)


def primes_list(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(str(i))
    return " ".join(primes)


def is_prime(n):
    prime = True
    floor_sqrt_n = int(n**(1/2.0))
    # slower when using:
    # for i in range(2, n):
    for i in range(2, floor_sqrt_n+1):  # more faster
        if n % i == 0:
            prime = False
    return prime


start = timeit.default_timer()
print("even list:", even_list(100))
print("primes list:", primes_list(100))
elapsed = (timeit.default_timer() - start)
print("time used: %.6f" % elapsed)
