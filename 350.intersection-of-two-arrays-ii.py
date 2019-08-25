#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = (nums1, nums2) if len(nums1) > len(nums2) else (nums2, nums1)

        n1 = "".join([str(n) for n in n1])
        n2 = "".join([str(n) for n in n2])

        count = n1.count(n2)

        return [int(n) for n in n2] * count
