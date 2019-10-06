#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
from typing import List


# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) >= 2 and nums[0] > nums[1]:
            return 0
        if len(nums) >= 2 and nums[-1] > nums[-2]:
            return len(nums) - 1

        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                return i

        return 0

    # @lc code=end
