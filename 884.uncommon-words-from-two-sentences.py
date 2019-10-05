#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

from typing import List


# @lc code=start
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a = A.split(" ")
        b = B.split(" ")

        d = {}
        for c in a:
            d[c] = d.get(c, 0) + 1
        for c in b:
            d[c] = d.get(c, 0) + 1

        return [c for c in d.keys() if d[c] == 1]

# @lc code=end
