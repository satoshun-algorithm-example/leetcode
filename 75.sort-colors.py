#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums:
            left = 0
            pivot = nums[-1]
            for i in range(len(nums)):
                if nums[i] < pivot:
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1

            nums[left], nums[-1] = nums[-1], nums[left]

            self.sortColors(nums[:left])
            self.sortColors(nums[left + 1:])
