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
        if not head or not head.next:
            return None

        slow = head.next
        fast = head.next.next

        while slow != fast:
            if not fast or not fast.next or not fast.next.next:
                return None
            slow = slow.next
            fast = fast.next.next

        start = head
        while start != fast:
            start = start.next
            fast = fast.next

        return start
