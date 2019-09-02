#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i, len(nums) - 1):
                if nums[j] != 0:
                    break
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
