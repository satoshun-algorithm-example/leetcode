#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True

        total = sum(nums)
        if total % 2 == 1:
            return False

        total = total // 2
        dp = [False for _ in range(total + 1)]
        dp[0] = True

        return dp[total]
