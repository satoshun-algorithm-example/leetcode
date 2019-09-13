#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r = []

        def check(now, start, remain):
            if remain == 0:
                r.append(now)
                return
            for i, candidate in enumerate(candidates[start:]):
                if remain - candidate >= 0:
                    check(now + [candidate], i + start, remain - candidate)

        check([], 0, target)

        return r
