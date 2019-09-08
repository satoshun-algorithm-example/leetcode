#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ab = {}
        for a in A:
            for b in B:
                ab[a + b] = ab.get(a + b, 0) + 1

        c = sum(ab.get(-c - d, 0) for c in C for d in D)
        return c
