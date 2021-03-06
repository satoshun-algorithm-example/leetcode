#
# @lc app=leetcode id=5238 lang=python3
#
# [5238]
#

# @lc code=start
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""
from typing import List


class Solution:
    def findSolution(self, customfunction, z: int) -> List[List[int]]:
        result = []
        for x in range(1, min(z, 1000) + 1):
            for y in range(1, min(z, 1000) + 1):
                if customfunction.f(x, y) == z:
                    result.append([x, y])

        return result

# @lc code=end
