#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                i += 1
        return i
