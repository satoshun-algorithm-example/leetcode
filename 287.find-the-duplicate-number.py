#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mid = (high + low) // 2
        while high - low > 1:
            count = 0
            for num in nums:
                if mid < num <= high:
                    count += 1

            if high - mid >= count:
                high = mid
            else:
                low = mid

            mid = (high + low) // 2
        return high
