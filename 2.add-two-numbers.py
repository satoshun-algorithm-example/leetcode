#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = 0
        i = 1
        while True:
            if l1 is None:
                break
            n1 += i * l1.val
            i *= 10
            l1 = l1.next

        n2 = 0
        i = 1
        while True:
            if l2 is None:
                break
            n2 += i * l2.val
            i *= 10
            l2 = l2.next

        s = n1 + n2
        if s == 0:
            return ListNode(0)

        head = None
        before = None
        while s:
            b = s % 10
            node = ListNode(b)
            if head is None:
                head = node
            if before is not None:
                before.next = node
            before = node
            s = s // 10
        return head

