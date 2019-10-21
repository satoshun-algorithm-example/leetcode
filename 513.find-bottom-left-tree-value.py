#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        depth = -1
        value = root.val

        def find(node, current_depth: int):
            nonlocal value, depth
            if not node:
                return

            if current_depth > depth:
                depth = current_depth
                value = node.val
            find(node.left, current_depth + 1)
            find(node.right, current_depth + 1)

        find(root, 0)
        return value

# @lc code=end
