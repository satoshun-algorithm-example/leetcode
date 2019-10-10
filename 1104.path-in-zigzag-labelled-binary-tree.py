#
# @lc app=leetcode id=1104 lang=python3
#
# [1104] Path In Zigzag Labelled Binary Tree
#
from typing import List


# @lc code=start
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if not label:
            return []

        if label == 1:
            return [label]

        path = [label]
        depth = 0
        while label >= depth ** 2:
            depth += 1

        while depth:
            if depth % 2 == 0:
                position = (((depth - 1) ** 2 + 1) // 2)
                label = label - position
            else:
                position = (((depth - 1) ** 2 + 1) // 2)
                label = label - position
            path.insert(0, label)
            depth -= 1
        return [1] + path

# @lc code=end
