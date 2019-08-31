#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = k
        for _ in range(len(nums) - 1):
            nums[0], nums[i % len(nums)] = nums[i % len(nums)], nums[0]
            i += k
