#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            if node.val > val and not node.left:
                node.left = TreeNode(val)
                break
            if node.val < val and not node.right:
                node.right = TreeNode(val)
                break

            if node.val > val:
                node = node.left
            else:
                node = node.right

        return root

# @lc code=end
