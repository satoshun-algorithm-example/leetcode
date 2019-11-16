#
# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#
from typing import List


# @lc code=start
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if L < M:
            L, M = M, L

        a_group = []
        for i in range(len(A) - L):
            a_group.append(sum(A[i:i + L]))

        b_group = []
        for i in range(len(A) - M):
            b_group.append(sum(A[i:i + M]))

        # check max a_group -> second b_group
        a_max = max(a_group)
        a_indices = [i for i in range(len(a_group)) if a_group[i] == a_max]
        b_max = 0
        for index in a_indices:
            start = max(0, index - L)
            end = index + L
            b_max = max(b_max, max(b_group[:start] + b_group[end:]))

        res = a_max + b_max

        # check max b_group -> second a_group
        b_max = max(b_group)
        b_indices = [i for i in range(len(b_group)) if b_group[i] == b_max]
        a_max = 0
        for index in b_indices:
            start = max(0, index - M)
            end = index + M
            a_max = max(a_max, max(a_group[:start] + a_group[end:]))

        return max(res, a_max + b_max)

# @lc code=end
