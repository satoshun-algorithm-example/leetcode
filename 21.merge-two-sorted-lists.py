#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head, current = None, None

        while True:
            if l1 is None and l2 is None:
                return head

            if l1 is None or (l2 is not None and l1.val >= l2.val):
                if current is not None:
                    current.next = l2
                current = l2
                l2 = l2.next
            else:
                if current is not None:
                    current.next = l1
                current = l1
                l1 = l1.next

            if head is None:
                head = current
