#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        l = 0
        n = head
        while n != None:
            l += 1
            n = n.next

        new_head = head
        current_head = head
        for i in range(k, l, k):
            current_head = self._sort(current_head, k-k)
            if k == 0:
                new_head = current_head
        return new_head

    def _sort(self, current: ListNode, k: int) -> ListNode:
        for _ in range(k - 1):
            before = current
            current = current.next
            current.next = before
        print(current)
        return current

