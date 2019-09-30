#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = nums[0]
        for i in range(len(nums)):
            if reach < i:
                break
            reach = max(reach, nums[i] + i)

        return reach >= len(nums) - 1

# @lc code=end
