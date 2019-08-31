#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = range(2, n)
        u = n ** 0.5
        i = 0
        while primes[0] < u:
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
            i += 1
        return i + len(primes)


def countPrimes2(n: int) -> int:
    if n < 3:
        return 0
    primes = range(2, n)
    u = n ** 0.5
    i = 0
    while primes[0] < u:
        prime = primes[0]
        primes = [p for p in primes if p % prime != 0]
        i += 1
    return i + len(primes)


def countPrimes1(n: int) -> int:
    primes = range(2, n)
    i = 0
    while primes:
        prime = primes[0]
        primes = [p for p in primes if p % prime != 0]
        i += 1

    return i
