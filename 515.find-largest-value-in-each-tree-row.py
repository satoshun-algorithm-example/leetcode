#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []

        leaves = [root]
        while leaves:
            res.append(max(v.val for v in leaves))
            leaves = [v.left for v in leaves if v.left] + [v.right for v in leaves if v.right]

        return res
# @lc code=end
