#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#
from typing import List


# @lc code=start
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]

        for y in range(1, len(B) + 1):
            for x in range(1, len(A) + 1):
                dp[y][x] = max(
                    dp[y - 1][x - 1] + (A[x - 1] == B[y - 1]),
                    dp[y - 1][x],
                    dp[y][x - 1],
                )

        return dp[-1][-1]

# @lc code=end
