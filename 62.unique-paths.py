#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l = m + n - 2

        r = 1
        for i in range(2, m):
            r *= i

        b = 1
        for i in range(m - 1):
            b *= (l - i)

        return b // r
