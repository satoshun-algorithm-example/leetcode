#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        dfs = [0, 0]
        stack = [root]
        while stack:
            new_stack = []
            value = 0
            for node in stack:
                value += node.val
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)

            l = len(dfs)
            dfs.append(max(dfs[l - 1], dfs[l - 2] + value))

            stack = new_stack

        return dfs[-1]
