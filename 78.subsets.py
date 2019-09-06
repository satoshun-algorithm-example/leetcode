#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[], nums]
        for i in range(1, len(nums)):
            result.extend(self._subset(nums, 0, i))
        return result

    def _subset(self, nums, left, rest):
        if rest == 1:
            r = []
            for i in range(left, len(nums)):
                r.append([nums[i]])
            return r

        r = []
        for i in range(left, len(nums) - rest + 1):
            r.extend([[nums[i]] + sub for sub in self._subset(nums, i + 1, rest - 1)])
        return r
