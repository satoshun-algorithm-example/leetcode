#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s:
            return []

        indices = []
        d = {}
        for c in p:
            d[c] = d.get(c, 0) + 1
        word_len = len(p)

        dd = {}
        for c in s[:word_len]:
            dd[c] = dd.get(c, 0) + 1

        for i in range(len(s) - word_len + 1):
            if i != 0:
                dd[s[i + word_len - 1]] = dd.get(s[i + word_len - 1], 0) + 1
                dd[s[i - 1]] -= 1
                if dd[s[i - 1]] == 0:
                    del dd[s[i - 1]]
            if d == dd:
                indices.append(i)

        return indices
