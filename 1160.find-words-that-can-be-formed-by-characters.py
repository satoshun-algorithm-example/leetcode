#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_dict = {}
        for c in chars:
            char_dict[c] = char_dict.get(c, 0) + 1

        l = 0
        for word in words:
            wd = {}
            for c in word:
                wd[c] = wd.get(c, 0) + 1

            ok = True
            for key in wd:
                if char_dict.get(key, 0) < wd[key]:
                    ok = False
                    break
            if ok:
                l += len(word)

        return l
