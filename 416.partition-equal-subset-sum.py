#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
from typing import List
from itertools import combinations


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        d = {i: num for i, num in enumerate(nums)}
        numbers = [i for i in range(len(nums))]
        for i in range(1, len(nums)):
            combs = combinations(numbers, i)
            for comb1 in combs:
                comb2 = [num for i, num in enumerate(nums) if i not in comb1]
                comb1 = [d.get(c) for c in comb1]
                if sum(comb1) == sum(comb2):
                    return True
        return False
