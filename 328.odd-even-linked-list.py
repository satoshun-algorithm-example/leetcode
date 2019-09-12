#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        current = head
        odd_head = current.next
        odd = odd_head
        while current.next and current.next.next:
            current.next, current = current.next.next, current.next.next
            odd.next, odd = current.next, current.next

        current.next = odd_head
        return head
