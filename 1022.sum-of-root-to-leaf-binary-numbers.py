#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.sum(root, "")

    def sum(self, node, b) -> int:
        b += str(node.val)
        if node.left and node.right:
            return self.sum(node.left, b) + self.sum(node.right, b)
        if node.left:
            return self.sum(node.left, b)
        if node.right:
            return self.sum(node.right, b)

        return int(b, 2)

    # @lc code=end
