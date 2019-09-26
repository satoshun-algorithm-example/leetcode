#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nth_node = head
        for _ in range(n):
            nth_node = nth_node.next

        start_node = head
        before = None
        while nth_node:
            nth_node = nth_node.next
            before = start_node
            start_node = start_node.next

        if not before:
            return start_node.next

        before.next = before.next.next
        return head
