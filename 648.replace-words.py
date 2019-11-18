#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#
from typing import List


# @lc code=start
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        sentences = sentence.split(" ")

        dict.sort()
        for i, s in enumerate(sentences):
            for d in dict:
                if s.startswith(d):
                    sentences[i] = d
                    break

        return " ".join(sentences)

# @lc code=end
