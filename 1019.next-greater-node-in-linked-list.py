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

        q = []
        for i in range(len(res)):
            while q:
                if q[0][0] < res[i]:
                    res[q[0][1]] = res[i]
                    q.pop(0)
                else:
                    break
            q.append([res[i], i])
            sorted(q)

        for i in q:
            res[i[1]] = 0

        return res

# @lc code=end
