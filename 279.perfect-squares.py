#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
import math
import sys


class Solution:
    def numSquares(self, n: int) -> int:
        m = sys.maxsize
        for start in range(1, int(math.sqrt(n))):
            current = n
            count = 0
            for end in range(start, 0, -1):
                a = end ** 2
                while current >= a:
                    current -= a
                    count += 1
                if current == 0:
                    break

            m = min(count, m)

        return m
