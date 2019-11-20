#
# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#
from typing import List


# @lc code=start
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        for i in range(1, len(A)):
            A[i] += A[i - 1]

        res = A[L + M - 1]
        l_max = A[L - 1]
        m_max = A[M - 1]
        for i in range(1, len(A) - L - M + 1):
            l_max = max(l_max, A[L + i - 1] - A[i - 1])
            m_max = max(m_max, A[M + i - 1] - A[i - 1])
            res = max(
                res,
                l_max + A[L + M + i - 1] - A[L + i - 1],
                m_max + A[L + M + i - 1] - A[M + i - 1],
            )

        return res

# @lc code=end
