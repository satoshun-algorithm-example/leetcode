#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
from typing import List


# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = []

        def can_transform(word1, word2):
            n = 0
            for i in range(len(word1)):
                n += word1[i] != word2[i]
            return n <= 1

        def check(current, index):
            if can_transform(current, endWord):
                return index

            for word in wordList:
                if word not in visited and can_transform(word, current):
                    visited.append(word)
                    v = check(word, index + 1)
                    if v:
                        return v

            return 0

        return check(beginWord, 2)

# @lc code=end
