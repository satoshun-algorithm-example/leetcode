#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)
