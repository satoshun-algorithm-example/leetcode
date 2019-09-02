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
        root.left = self.sortedArrayToBST(nums[:center])
        root.right = self.sortedArrayToBST(nums[center + 1:])
        return root
