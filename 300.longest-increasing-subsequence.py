#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        height = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    height[i] = max(height[j] + 1, height[i])
        return max(height)
