#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
class Solution:
    def countPrimes(self, n: int) -> int:
        primes = range(2, n)
        i = 0
        while primes:
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
            i += 1

        return i
