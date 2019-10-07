#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        m = 0

        def search(node, parents):
            nonlocal m

            if not node:
                return
            for parent in parents:
                mm = abs(parent.val - node.val)
                if mm > m:
                    m = mm
            search(node.left, parents + [node])
            search(node.right, parents + [node])

        search(root, [])
        return m

# @lc code=end
