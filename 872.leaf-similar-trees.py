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
        def dig(node, target):
            if not node:
                return
            if not node.left and not node.right:
                target.append(node.val)
                return

            dig(node.left, target)
            dig(node.right, target)

        leaf1 = []
        dig(root1, leaf1)
        leaf2 = []
        dig(root2, leaf2)
        return leaf1 == leaf2
