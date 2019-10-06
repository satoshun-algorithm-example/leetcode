#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
from typing import List


# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid1 = (low + high) // 2
            mid2 = mid1 + 1

            # if nums[mid1] > nums[mid2]:
            #     return mid1

            if nums[mid1] < nums[mid2]:
                low = mid2
            else:
                high = mid1
        return low

    # @lc code=end
