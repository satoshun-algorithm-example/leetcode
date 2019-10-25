#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        value = sum(nums)
        if (value % 2) == 1:
            return False

        value = value // 2

        dp = []
        for i in range(len(nums) + 1):
            dp.append([False] * (value + 1))
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, value + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        return dp[len(nums)][value]
