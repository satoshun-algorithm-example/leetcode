#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#
from typing import List


# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda a: a[1])
        count = 1
        next_value = pairs[0][1]
        pairs = pairs[1::]
        while True:
            find = False
            for pair in pairs:
                if next_value < pair[0]:
                    # TODO remove from pairs
                    next_value = pair[1]
                    find = True
                    count += 1
                    break

            if not find:
                break

        return count

# @lc code=end
