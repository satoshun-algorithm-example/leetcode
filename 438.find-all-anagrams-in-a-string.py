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
        p = sorted(p)
        word_len = len(p)
        for i in range(len(s) - word_len + 1):
            if sorted(s[i:i + word_len]) == p:
                indices.append(i)

        return indices
