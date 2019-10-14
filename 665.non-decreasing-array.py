#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#
from typing import List


# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        c = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if i - 2 < 0:
                    nums[i - 1] = nums[i]
                elif nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                c += 1

        return c <= 1
# @lc code=end
