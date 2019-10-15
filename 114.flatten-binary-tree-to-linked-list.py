#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []

        def search(node):
            if not node:
                return
            nodes.append(node)
            if node.left:
                search(node.left)
            if node.right:
                search(node.right)

        search(root)

        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].right = nodes[i - 1]

# @lc code=end
