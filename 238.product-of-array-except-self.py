#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        original = nums.copy()
        nums[0] = reduce(lambda x, y: x * y, original[1:])
        for i in range(1, len(nums)):
            if nums[i] == 0:
                nums[i] = nums[i - 1] * original[i - 1]
            else:
                nums[i] = nums[i - 1] * original[i - 1] // nums[i]
        return nums
