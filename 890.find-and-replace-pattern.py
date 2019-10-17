#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#
from typing import List


# @lc code=start
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        groups = {}
        for i, p in enumerate(pattern):
            groups[p] = groups.get(p, []) + [i]

        groups = groups.values()

        res = []
        for word in words:
            for group in groups:
                before = None
                is_not_match = False
                checked_char = set()

                for index in group:
                    if before is not None or word[index] != before:
                        is_not_match = True
                        break
                    if before is None:
                        before = word[index]
                        if before in checked_char:
                            is_not_match = True
                            break
                        checked_char.add(before)
                    else:
                        before = word[index]

                if not is_not_match:
                    res.append(word)

        return res
# @lc code=end
