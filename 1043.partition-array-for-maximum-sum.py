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
            m = 0
            for j in range(K):
                if i - j - 1 < 0:
                    dp[i] = max(dp[i], (j + 1) * m)
                    break
                m = max(m, A[i - j])
                dp[i] = max(dp[i], dp[i - j - 1] + (j + 1) * m)

        return dp[-1]
# @lc code=end
