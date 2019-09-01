#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.max_depth = 1

        def count(node, cur_depth):
            if node.left is None and node.right is None:
                self.max_depth = max(self.max_depth, cur_depth)
                return

            if node.left:
                count(node.left, cur_depth + 1)
            if node.right:
                count(node.right, cur_depth + 1)

        count(root, 1)
        return self.max_depth
