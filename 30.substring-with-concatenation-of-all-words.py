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

        total = []

        for i in range(len(s)):
            if self.find_prefix(s, str):
                total.append(i)

        return total

    def find_prefix(self, s: str, words):
        if not words and not s:
            return True
        if not words or not s:
            return False

        for i in range(len(words)):
            if s.startswith(words[i]):
                if self.find_prefix(s[len(words[i]):], words[:i] + words[i + 1:]):
                    return True

        return False
