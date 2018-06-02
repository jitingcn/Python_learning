#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - 180530_note.py
# Created by JT on 30/05/2018 10:11.
import math
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
    elif m == 4:
        primes_l = sieve_atkin(n)
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


def sieve_atkin(nmax):  # from: https://gist.github.com/mineta/7840849
    """
    Returns a list of prime numbers below the number "n"
    """
    prime_list = dict([(i, False) for i in range(5, nmax+1)])
    for x in range(1, int(math.sqrt(nmax))+1):
        for y in range(1, int(math.sqrt(nmax))+1):
            n = 4*x**2 + y**2
            if (n <= nmax) and ((n % 12 == 1) or (n % 12 == 5)):
                prime_list[n] = not prime_list[n]
            n = 3*x**2 + y**2
            if (n <= nmax) and (n % 12 == 7):
                prime_list[n] = not prime_list[n]
            n = 3*x**2 - y**2
            if (x > y) and (n <= nmax) and (n % 12 == 11):
                prime_list[n] = not prime_list[n]
    for n in range(5, int(math.sqrt(nmax))+1):
        if prime_list[n]:
            ik = 1
            while ik * n**2 <= nmax:
                prime_list[ik * n**2] = False
                ik += 1
    prime = []
    for i in range(nmax + 1):
        if i in [0, 1, 4]:
            pass
        elif i in [2, 3] or prime_list[i]:
            prime.append(i)
        else:
            pass
    return prime


def main(c=10, r=10000):
    print("even list:", even_list(100))
    print("primes list:", primes_list(1000, 2))
    print("\nPrime Number: ")
    for a in range(5):
        msg = ""
        if a == 0:
            msg = "Trial Division"
        elif a == 1:  # method 1: slow
            msg = "Sieve of Eratosthenes"
        elif a == 2:  # method 2: more faster
            msg = "Another Sieve of Eratosthenes"
        elif a == 3:  # method 3: faster
            msg = "Python filter() and generator() from https://github.com/michaelliao/learn-python3" \
                  "/blob/master/samples/functional/prime_numbers.py"
        elif a == 4:
            msg = "Sieve of Atkin from: https://gist.github.com/mineta/7840849"
        print("\nMethod %d: %s" % (a + 1, msg))
        len_list = []
        start = timeit.default_timer()
        for b in range(c):
            len_list = primes_list(r, a)
        elapsed = (timeit.default_timer() - start) / c
        print("length:", len(len_list))
        print(c, "calculations average time: %.6f s" % elapsed)


if __name__ == '__main__':
    main()
