#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dig(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]

            return dig(node.left) + dig(node.right)

        return dig(root1) == dig(root2)
