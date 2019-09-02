#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        center = len(nums) // 2
        root = TreeNode(nums[center])
        self.recursive_left(nums[:center], root)
        self.recursive_right(nums[center + 1:], root)
        return root

    def recursive_left(self, nums, parent):
        if not nums:
            return
        center = len(nums) // 2
        node = TreeNode(nums[center])
        parent.left = node
        self.recursive_left(nums[:center], node)
        self.recursive_right(nums[center + 1:], node)

    def recursive_right(self, nums, parent):
        if not nums:
            return
        center = len(nums) // 2
        node = TreeNode(nums[center])
        parent.right = node
        self.recursive_left(nums[:center], node)
        self.recursive_right(nums[center + 1:], node)
