#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
from typing import List


# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        depth = 1
        queue = [beginWord]

        def can_transform(word1, word2):
            n = 0
            for i in range(len(word1)):
                n += word1[i] != word2[i]

            return n == 1

        while queue:
            for _ in range(len(queue)):
                word = queue.pop()
                if word == endWord:
                    return depth + 1

                append = []
                for w in wordList:
                    if can_transform(w, word):
                        queue.append(w)
                        append.append(w)

                for w in append:
                    wordList.remove(w)

            depth += 1

        return 0

# @lc code=end
