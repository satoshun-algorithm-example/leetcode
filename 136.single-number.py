#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums) // 2):
            if nums[i * 2] != nums[i * 2 + 1]:
                return nums[i * 2]

        return nums[-1]
