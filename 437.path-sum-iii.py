#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.total = 0
        self.sum = sum

        self.dfs(root)
        return self.total

    def dfs(self, node):
        if node is None:
            return

        self._dfs(node, 0)
        self.dfs(node.left)
        self.dfs(node.right)

    def _dfs(self, node, value):
        if node is None:
            return

        value += node.val
        if self.sum == value:
            self.total += 1

        self._dfs(node.left, value)
        self._dfs(node.right, value)
