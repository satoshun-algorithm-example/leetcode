#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        indices = [0 for _ in range(len(matrix))]

        kk = 0
        while True:
            next_value = -1
            next_i = -1

            for i, index in enumerate(indices):
                m = matrix[i]
                if len(m) <= index:
                    continue
                value = m[index]
                if next_value == -1 or value < next_value:
                    next_value = value
                    next_i = i

            indices[next_i] += 1
            kk += 1

            if kk == k:
                return next_value
