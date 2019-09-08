#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[i] == nums[(j + i + 1) % len(nums)]:
                    return nums[i]
