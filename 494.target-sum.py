#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        d = {}
        nums.sort()
        return self.check(nums, -S, d)

    def check(self, nums, number, d):
        if not nums:
            return number == 0

        key = (len(nums), number)
        cache = d.get(key)
        if cache is not None:
            return cache

        v = nums[0]
        result = self.check(nums[1:], number - v, d) + self.check(nums[1:], number + v, d)
        d[key] = result
        return result
