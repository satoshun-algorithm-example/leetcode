#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        half = n // 2
        is_even = n % 2 == 0

        i1 = 0
        i2 = 0
        c = 0
        b = 0
        for i in range(n):
            n1 = nums1[i1] if i1 < len(nums1) else None
            n2 = nums2[i2] if i2 < len(nums2) else None
            if n1 is None:
                b = c
                c = n2
                i2 += 1
            elif n2 is None:
                b = c
                c = n1
                i1 += 1
            elif n1 < n2:
                b = c
                c = n1
                i1 += 1
            else:
                b = c
                c = n2
                i2 += 1

            if half == i:
                if is_even:
                    c = (c + b) / 2
                break

        return float(c)

