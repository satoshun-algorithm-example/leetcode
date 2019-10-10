#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a < 0 or b < 0:
            # TODO subtract
            return a + b

        while b:
            tmp = a & b
            a = a ^ b
            b = tmp << 1
        return a
