#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
from typing import List
import sys


# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = []

        if endWord not in wordList:
            return 0

        def can_transform(word1, word2):
            n = 0
            for i in range(len(word1)):
                n += word1[i] != word2[i]
            return n <= 1

        def check(current, index):
            if can_transform(current, endWord):
                return index

            result = sys.maxsize
            for word in wordList:
                if word not in visited and can_transform(word, current):
                    visited.append(word)
                    result = min(result, check(word, index + 1))

            return result

        result = check(beginWord, 2)
        if result == sys.maxsize:
            return 0
        return result

# @lc code=end
