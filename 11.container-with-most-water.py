#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        l = len(height)

        for x in range(l):
            for y in range(x + 1, l):
                mm = (y - x) * min(height[x], height[y])
                if mm > m:
                    m = mm

        return m
