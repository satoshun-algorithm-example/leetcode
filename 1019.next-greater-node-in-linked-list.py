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
        node = head
        while node:
            res.append(node.val)
            node = node.next

        for i in range(len(res)):
            have = False
            for j in range(i + 1, len(res)):
                if res[i] < res[j]:
                    res[i] = res[j]
                    have = True
                    break
            if not have:
                res[i] = 0

        return res

# @lc code=end
