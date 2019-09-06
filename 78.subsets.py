#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [r + [num] for r in result]
        return result
