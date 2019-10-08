#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.calculate(root, 0, sys.maxsize)

    def calculate(self, node, mx, mi):
        if not node:
            return mx - mi

        mx = max(node.val, mx)
        mi = min(node.val, mi)
        return max(
            self.calculate(node.left, mx, mi),
            self.calculate(node.right, mx, mi),
        )

# @lc code=end
