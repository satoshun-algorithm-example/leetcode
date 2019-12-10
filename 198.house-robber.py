#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in nums] + [0, 0]
        for i in range(2, len(nums) + 2):
            dp[i] = max(dp[i - 2] + nums[i - 2], dp[i - 1])

        return dp[-1]
