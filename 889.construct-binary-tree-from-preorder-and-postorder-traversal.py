#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        pre_index, pos_index = 0, 0

        def search():
            nonlocal pre_index, pos_index
            root = TreeNode(pre[pre_index])
            pre_index += 1
            if root.val != post[pos_index]:
                root.left = search()
            if root.val != post[pos_index]:
                root.right = search()
            pos_index += 1
            return root

        return search()

# @lc code=end
