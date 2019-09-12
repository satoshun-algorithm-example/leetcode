#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in d:
                d[key] = []
            d[key].append(s)

        return list(d.values())
