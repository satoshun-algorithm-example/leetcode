#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        for i in range(len(nums)):
            permutations += self.permutations(nums[i], nums[:i] + nums[i + 1:])

        return permutations

    def permutations(self, v, nums):
        if not nums:
            return [[v]]

        permutations = []
        for i in range(len(nums)):
            permutations += [[v] + p for p in self.permutations(nums[i], nums[:i] + nums[i + 1:])]
        return permutations
