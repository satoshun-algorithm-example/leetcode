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
            ss = ''.join(sorted(s))
            if ss not in d:
                d[ss] = []
            d[ss].append(s)

        return list(d.values())
