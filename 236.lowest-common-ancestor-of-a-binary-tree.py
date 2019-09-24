#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # fast path
        is_q = self.same_path(q, p)
        if is_q:
            return q

        while True:
            is_p = self.same_path(p, q)
            if is_p:
                return p

            p = self.get_parent(root, p)

    def get_parent(self, node, p):
        if not node:
            return None

        if node.left:
            if node.left.val == p.val:
                return node

        if node.right:
            if node.right.val == p.val:
                return node

        return self.get_parent(node.left, p) or self.get_parent(node.right, p)

    def same_path(self, node, target):
        if not node:
            return None

        if node.val == target.val:
            return node

        return self.same_path(node.left, target) or self.same_path(node.right, target)
