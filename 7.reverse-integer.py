#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            is_minus = True
            x = abs(x)
        else:
            is_minus = False

        r, size = 0, len(str(x))

        for i in range(size):
            d = x % 10
            r += d * 10 ** (size - i - 1)
            x //= 10

        if is_minus:
            r = -r

        if abs(r) > ((1 << 31) - 1):
            return 0

        return r
