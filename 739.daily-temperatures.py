#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        tl = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                b = stack.pop()
                tl[b] = i - b
            stack.append(i)

        return tl
