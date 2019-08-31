#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        start = 0
        end = len(sort_nums) - 1

        while start <= end:
            if nums[start] != sort_nums[start]:
                break
            start += 1

        while start <= end:
            if nums[end] != sort_nums[end]:
                break
            end -= 1

        return end - start + 1
