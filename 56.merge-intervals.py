#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        while len(intervals) > i:
            target = intervals[i]
            i += 1
            while len(intervals) > i and \
                    ((intervals[i][0] <= target[0] <= intervals[i][1]) or
                     (intervals[i][0] <= target[1] <= intervals[i][1]) or
                     (target[0] <= intervals[i][0] <= target[1]) or
                     (target[0] <= intervals[i][1] <= target[1])):
                target[0] = min(target[0], intervals[i][0])
                target[1] = max(target[1], intervals[i][1])
                i += 1

            res.append(target)
        return res
