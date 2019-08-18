#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        cur = prev = 0

        for num in nums:
            tmp = cur
            cur = max(prev + num, cur)
            prev = tmp
        return cur
