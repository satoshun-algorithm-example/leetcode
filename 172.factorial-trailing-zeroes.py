#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = n // 5
        if i == 0:
            return 0
        return i + self.trailingZeroes(i)
