#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())
