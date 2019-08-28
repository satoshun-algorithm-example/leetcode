#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        for _ in range(n + m):
            if n <= j:
                break

            if m <= i:
                nums1[i + j] = nums2[j]
                j += 1
                continue

            if nums1[i + j] > nums2[j]:
                nums1[i + j + 1:] = nums1[i + j:-1]
                nums1[i + j] = nums2[j]
                j += 1
            else:
                i += 1
