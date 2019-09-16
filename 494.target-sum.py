#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        return self.check(nums, -S)

    def check(self, nums, number):
        if not nums:
            return number == 0

        v = nums[0]
        return self.check(nums[1:], number - v) + self.check(nums[1:], number + v)
