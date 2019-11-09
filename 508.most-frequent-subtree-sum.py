#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
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
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        values = {}

        def loop(node):
            if not node:
                return
            i = calculate(node, 0)
            values[i] = values.get(i, 0) + 1
            loop(node.left)
            loop(node.right)

        def calculate(node, i):
            if not node:
                return i

            i += node.val
            i = calculate(node.left, i)
            i = calculate(node.right, i)
            return i

        loop(root)

        if not values:
            return []

        m = max(values.values())
        return [key for key, val in values.items() if val == m]

# @lc code=end
