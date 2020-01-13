#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
from typing import List


# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        def can_transform(word1, word2):
            n = 0
            for i in range(len(word1)):
                n += word1[i] != word2[i]

            return n == 1

        queue = [beginWord]
        depth = 1
        visited = set()

        while queue:
            for _ in range(len(queue)):
                word = queue.pop(0)
                if word == endWord:
                    return depth

                for i in range(len(word)):
                    for c in range(26):
                        c = chr(ord('a') + c)
                        w = word[:i] + c + word[i + 1:]
                        if w in wordList and w not in visited:
                            visited.add(w)
                            queue.append(w)

            depth += 1

        return 0

# @lc code=end
