#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        last = head
        count = 1
        while last.next:
            last = last.next
            count += 1

        head = self.sort(head, last)
        return head

    def sort(self, head, last):
        if not head or not last:
            return head
        if head.val == last.val:
            return head
        before = None
        current = head
        new_last = last
        while current and current.val != last.val:
            if last.val < current.val:
                if not before:
                    head = current.next
                    current.next = new_last.next
                    new_last.next = current
                    new_last = current

                    current = head
                    continue
                else:
                    before.next = current.next
                    current.next = new_last.next
                    new_last.next = current
                    new_last = current
                    current = before.next
                    continue
            else:
                before = current
            current = current.next

        head = self.sort(head, before)
        self.sort(last, new_last)
        #  [4,19,14,5,-3,1,8,5,11,15]

        return head
