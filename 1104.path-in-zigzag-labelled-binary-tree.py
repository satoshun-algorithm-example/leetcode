#
# @lc app=leetcode id=1104 lang=python3
#
# [1104] Path In Zigzag Labelled Binary Tree
#
from typing import List


# @lc code=start
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        depth = 1
        while label >= 2 ** depth:
            depth += 1

        while label:
            res.insert(0, label)
            label = ((2 ** depth - 1) + (2 ** (depth - 1)) - label) // 2
            depth -= 1

        return res

# @lc code=end
