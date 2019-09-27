#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        for i, num in enumerate(nums):
            if num == target:
                if start == -1:
                    start = i
                else:
                    end = i
        if start != -1 and end == -1:
            end = start

        return [start, end]
