#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mark = [False for _ in range(len(nums))]
        mark[len(nums) - 1] = True
        i = len(nums) - 2
        while i >= 0:
            for j in range(1, nums[i] + 1):
                if len(mark) > i + j and mark[i + j]:
                    mark[i] = True
                    break
            i -= 1

        return mark[0]

# @lc code=end
