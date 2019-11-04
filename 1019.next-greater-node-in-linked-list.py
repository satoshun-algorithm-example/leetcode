#
# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        stack = []
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack[-1][0]] = head.val
                stack.pop()
            stack.append([len(res), head.val])
            res.append(0)

            head = head.next

        return res

# @lc code=end
