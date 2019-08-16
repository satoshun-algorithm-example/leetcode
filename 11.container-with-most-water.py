#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        size = len(height)
        left = 0
        right = size - 1

        for d in range(size - 1, 0, -1):
            if height[left] < height[right]:
                m, left = max(m, height[left] * d), left + 1
            else:
                m, right = max(m, height[right] * d), right - 1

        return m
