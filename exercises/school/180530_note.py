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


def primes_list(n, m):
    primes_l = []
    if m == 0:
        for i in range(2, n + 1):
            if is_prime(i):
                primes_l.append(i)
    elif m == 1:
        primes_l = primes_sieve(n)
    elif m == 2:
        for i in range(2, n + 1):
            if prime_sieve(i):
                primes_l.append(i)
    elif m == 3:
        for i in primes():
            if i < n:
                primes_l.append(i)
            else:
                break
    return primes_l


def is_prime(n):
    prime = True
    sqrt_n = int(n**(1/2.0))
    # slower when using:
    # for i in range(2, n):
    for i in range(2, sqrt_n+1):  # faster
        if n % i == 0:
            prime = False
    return prime


def prime_sieve(n):
    if n > 2 and n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def primes_sieve(n):
    num_list = list(range(2, n+1))
    length = len(num_list)
    i = 0
    while i < length:
        ni = num_list[i]
        '''if num_list[i] > 2 and num_list[i] % 2 == 0:
            num_list.pop(i)
            length -= 1
        else:'''
        o = 1
        while o < length:
            # if num_list[o] % ni == 0: will delete "ni" self
            if num_list[o] % ni == 0 and num_list[o] != ni:
                num_list.pop(o)
                length -= 1
            o += 1
        i += 1
    return num_list


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


def main(c=10, r=10000):
    print("even list:", even_list(100))
    print("primes list:", primes_list(1000, 2))
    print("\nPrime Number: ")
    for a in range(4):
        msg = "do nothing"
        if a == 0:
            msg = "Trial Division"
        elif a == 1:  # method 1: slow
            msg = "Sieve of Eratosthenes"
        elif a == 2:  # method 2: more faster
            msg = "Another Sieve of Eratosthenes"
        elif a == 3:  # method 3: faster
            msg = "Python filter() and generator() from https://github.com/michaelliao/learn-python3" \
                  "/blob/master/samples/functional/prime_numbers.py"
        len_list = []
        start = timeit.default_timer()
        for b in range(c):
            len_list = primes_list(r, a)
        elapsed = (timeit.default_timer() - start) / 100
        print("\nMethod %d: %s" % (a + 1, msg))
        print("length:", len(len_list))
        print(c, "calculations average time: %.6f s" % elapsed)


if __name__ == '__main__':
    main()
