#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fuctorial(v):
            i = 1
            for b in range(2, v + 1):
                i *= b
            return i

        f = fuctorial(n)

        def countup(s):
            i = 0
            for c in s[::-1]:
                if c != '0':
                    break
                i += 1
            return i

        return countup(str(f))
