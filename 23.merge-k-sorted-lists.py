#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        s = []
        for l in lists:
            e = l
            while e:
                s += [e.val]
                e = e.next
        if not s:
            return None
        s = sorted(s)
        head = ListNode(s[0])
        current = head
        for e in s[1:]:
            current.next = ListNode(e)
            current = current.next
        return head

