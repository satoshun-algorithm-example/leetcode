#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        if b == 0:
            return a

        while b:
            carry = a & b
            a = a ^ b
            b = carry << 1

        return a
