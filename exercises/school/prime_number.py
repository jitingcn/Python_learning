#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import timeit


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


def main(c=3, r=1000000):
    print("\nPrime Number: ")
    len_list = []
    start = timeit.default_timer()
    for b in range(c):
        len_list = prime(r)
    elapsed = (timeit.default_timer() - start) / c
    print("length:", len(len_list))
    print(c, "calculations average time: %.6f s" % elapsed)
    print("Max prime number in %d: %d\n" % (r, len_list[-1]))


if __name__ == '__main__':
    try:
        main(int(input("Enter test times: ")), int(input("Enter test range:")))
    except Exception as e:
        print(e)
