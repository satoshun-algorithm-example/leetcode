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

        word = words[0]
        max_len = len(word) * len(words)
        total = []
        for i in range(len(s) - max_len + 1):
            if self.find_prefix(s[i:], words):
                total.append(i)

        return total

    def find_prefix(self, s: str, words):
        if not words:
            return True
        if not s:
            return False

        checked = []
        for i in range(len(words)):
            if words[i] in checked:
                continue
            if s.startswith(words[i]):
                return self.find_prefix(s[len(words[i]):], words[:i] + words[i + 1:])
            checked.append(words[i])

        return False
