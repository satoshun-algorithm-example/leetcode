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

        cache = []
        return self.find_word(s, 0, d, cache)

    def find_word(self, s, start, rest_words, cache):
        if len(s) == start:
            return True

        if start in cache:
            return False
        cache.append(start)

        for word in rest_words.keys():
            if s[start:start + len(word)] == word:
                if self.find_word(s, start + len(word), rest_words, cache):
                    return True

        return False
