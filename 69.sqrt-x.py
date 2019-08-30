#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while True:
            m = (l + r) // 2
            if m * m <= x < (m + 1) * (m + 1):
                return m

            if m * m > x:
                r = m - 1
            else:
                l = m + 1
