#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#
from typing import List


# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        if K == 1:
            return sum(A)
        if not A:
            return 0

        dp = [0] * len(A)
        dp[0] = A[0]
        for i in range(1, len(A)):
            m = dp[i - 1] + A[i]
            for j in range(K):
                if i - j - 1 < 0:
                    break

                m = max(m, dp[i - j - 1] + (j + 1) * A[i])
            dp[i] = m

        return dp[-1]
# @lc code=end
