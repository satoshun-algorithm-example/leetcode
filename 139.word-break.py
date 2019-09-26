#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = {}
        for word in wordDict:
            d[word] = d.get(word, 0) + 1

        return self.find_word(s, 0, d)

    def find_word(self, s, start, rest_words):
        if len(s) == start:
            return True

        for word in rest_words.keys():
            if s[start:start + len(word)] == word:
                if self.find_word(s, start + len(word), rest_words):
                    return True

        return False
