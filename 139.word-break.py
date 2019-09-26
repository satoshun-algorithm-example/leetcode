#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words_len = sum(len(word) for word in wordDict)
        d = {}
        for word in wordDict:
            d[word] = d.get(word, 0) + 1
        for i in range(len(s) - words_len + 1):
            dd = d.copy()
            if self.find_word(s, i, i + words_len, dd):
                return True

        return False

    def find_word(self, s, start, end, rest_words):
        if not rest_words:
            return True

        for word in rest_words.keys():
            if s[start:start + len(word)] == word:
                words = rest_words.copy()
                words[word] -= 1
                if words[word] == 0:
                    del words[word]
                if self.find_word(s, start + len(word), end, words):
                    return True

        return False
