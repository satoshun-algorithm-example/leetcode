#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
from typing import List


# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                res.append(index + 1)
            nums[index] = -nums[index]

        return res
# @lc code=end
