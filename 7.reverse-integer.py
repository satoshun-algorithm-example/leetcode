#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            is_minus = -1
        else:
            is_minus = 1

        x = int(str(x * is_minus)[::-1])
        return is_minus * x * (x < 2 ** 31)
