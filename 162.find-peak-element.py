#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
from typing import List


# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

    # @lc code=end
