#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        nodes = [root]
        while nodes:
            new_nodes = []
            is_failed = False
            for node in nodes:
                if not node.left and node.right:
                    is_failed = True
                    break
                if not node.left and not node.right:
                    if is_failed:
                        return False
                    is_failed = True
                    break
                if node.left and not node.right:
                    if is_failed:
                        return False
                    is_failed = True
                    break

                if is_failed:
                    return False

                new_nodes += [node.left, node.right]

            nodes = new_nodes

        return True

# @lc code=end
