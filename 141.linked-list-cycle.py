#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
class Solution:
    def hasCycle(self, head):
        mark = []

        while head:
            if head in mark:
                return True
            mark.append(head)
            head = head.next

        return False
