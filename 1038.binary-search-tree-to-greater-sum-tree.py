#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        current = 0

        def search(node):
            nonlocal current

            if not node:
                return

            if node.right:
                search(node.right)

            current += node.val
            node.val = current

            if node.left:
                search(node.left)

        search(root)
        return root
# @lc code=end
