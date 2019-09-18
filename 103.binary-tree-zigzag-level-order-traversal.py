#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        nodes = [[root.val]]
        is_left = False
        stack = []
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)

        while stack:
            new_stack = []
            n = []
            if is_left:
                while stack:
                    s = stack.pop()
                    n.append(s.val)
                    if s.left:
                        new_stack.append(s.left)
                    if s.right:
                        new_stack.append(s.right)
            else:
                while stack:
                    s = stack.pop()
                    n.append(s.val)
                    if s.right:
                        new_stack.append(s.right)
                    if s.left:
                        new_stack.append(s.left)
            nodes.append(n)
            is_left = not is_left
            stack = new_stack

        return nodes
