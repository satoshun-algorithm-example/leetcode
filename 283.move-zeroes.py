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
        position = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[position] = nums[position], nums[i]
                position += 1
