#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1007
# 2019/2/19 Jiting
"""
1007 素数对猜想 （20 point(s)）
让我们定义dn为：d n=p (n+1)−p n，其中p i是第i个素数。显然有d 1=1，且对于n>1有d n是偶数。“素数对猜想”认为“存在无穷多对相邻且差为2的素数”。
现给定任意正整数N(<10^5)，请计算不超过N的满足猜想的素数对的个数。

输入格式:
输入在一行给出正整数N。

输出格式:
在一行中输出不超过N的满足猜想的素数对的个数。

输入样例:
20
输出样例:
4
"""
from itertools import compress


def rwh_primes1v2(n):  # https://stackoverflow.com/a/46635266
    """ Returns a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1, int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


prime_list = rwh_primes1v2(int(input())+1)
# print(prime_list)
couple = 0

for j in range(1, len(prime_list)+1):
    if j == len(prime_list):
        break
    if prime_list[-j] - prime_list[-j-1] == 2:
        couple += 1

print(couple)
