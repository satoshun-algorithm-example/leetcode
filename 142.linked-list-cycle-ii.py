#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        elements = [head]
        slow = head
        while slow:
            slow = slow.next
            if slow in elements:
                return slow
            elements.append(slow)

        return None
