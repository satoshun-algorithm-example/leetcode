#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        tl = [0] * len(T)

        for i in range(len(T)):
            c = 1
            for j in range(i + 1, len(T)):
                if T[i] < T[j]:
                    tl[i] = c
                    break
                c += 1

        return tl
