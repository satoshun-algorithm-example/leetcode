#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        # create separated list
        node = root
        parts = [[] for _ in range(k)]
        i = 0
        while node:
            parts[i].append(node)
            i = (i + 1) % k
            node = node.next

        # divide
        res = [[] for _ in range(k)]
        nums = [len(part) for part in parts]
        n = 0
        for i in range(k):
            num = nums[i]
            for _ in range(num):
                res[i].append(parts[n].pop(0))
                n = (n + 1) % k

        return res

# @lc code=end
