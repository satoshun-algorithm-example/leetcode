#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
