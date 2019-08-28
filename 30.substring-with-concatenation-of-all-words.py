#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
from typing import List
import re


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []

        word = words[0]
        words = words[1:]
        indices = [m.start() for m in re.finditer(word, word)]
        for i in indices:
            pass
