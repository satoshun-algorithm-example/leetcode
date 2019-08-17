#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        a = []
        if root.left is not None:
            a.append(self.max_depth(root.left, 1))
        if root.right is not None:
            a.append(self.max_depth(root.right, 1))

        return sum(a)

    def max_depth(self, node, depth):
        a = [depth]
        if node.left is not None:
            a.append(self.max_depth(node.left, depth + 1))
        if node.right is not None:
            a.append(self.max_depth(node.right, depth + 1))
        return max(a)
