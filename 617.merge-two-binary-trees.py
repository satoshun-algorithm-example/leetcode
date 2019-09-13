#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def sum_node(a1, a2):
            a1.val += a2.val

            if a1.left or a2.left:
                if not a1.left:
                    a1.left = TreeNode(0)
                if not a2.left:
                    a2.left = TreeNode(0)
                sum_node(a1.left, a2.left)

            if a1.right or a2.right:
                if not a1.right:
                    a1.right = TreeNode(0)
                if not a2.right:
                    a2.right = TreeNode(0)
                sum_node(a1.right, a2.right)

        if not t1:
            return t2
        if not t2:
            return t1

        sum_node(t1, t2)
        return t1
