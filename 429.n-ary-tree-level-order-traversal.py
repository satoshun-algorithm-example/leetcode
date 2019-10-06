#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        if not root:
            return []

        levels = []
        stack = [root]
        while stack:
            levels.append([])
            nodes = [s for s in stack]
            stack = []
            for node in nodes:
                levels[-1].append(node.val)
                if node.children:
                    stack.extend(node.children)

        return levels

# @lc code=end
