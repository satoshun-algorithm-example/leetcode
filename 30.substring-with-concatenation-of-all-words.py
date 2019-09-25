#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        d = {}
        for w in words:
            d[w] = d.get(w, 0) + 1

        word = words[0]
        max_len = len(word) * len(words)
        total = []
        for i in range(len(s) - max_len + 1):
            dd = d.copy()
            if self.find_prefix(s[i:], dd):
                total.append(i)

        return total

    def find_prefix(self, s: str, d: dict):
        if not d:
            return True
        if not s:
            return False

        for key in d.keys():
            if s.startswith(key):
                d[key] -= 1
                if d[key] == 0:
                    del d[key]
                return self.find_prefix(s[len(key):], d)

        return False
