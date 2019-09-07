#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
from typing import List
from itertools import permutations


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ab = [A[a] + B[b] for a in range(len(A)) for b in range(len(B))]
        cd = [C[a] + D[b] for a in range(len(C)) for b in range(len(D))]

        c = 0
        for i in range(len(ab)):
            for j in range(len(cd)):
                if ab[i] == -cd[j]:
                    c += 1

        return c
