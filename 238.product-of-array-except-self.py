#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        d = 1
        for num in nums:
            products.append(d)
            d *= num

        d = 1
        for i, num in enumerate(nums[::-1]):
            products[len(nums) - 1 - i] *= d
            d *= num

        return products
