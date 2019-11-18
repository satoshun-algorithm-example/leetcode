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
        alphabet_map = {}
        for d in dict:
            alphabet_map[d[0]] = alphabet_map.get(d[0], []) + [d]

        for i, s in enumerate(sentences):
            dd = alphabet_map.get(s[0], [])
            for d in dd:
                if s.startswith(d):
                    sentences[i] = d
                    break

        return " ".join(sentences)

# @lc code=end
