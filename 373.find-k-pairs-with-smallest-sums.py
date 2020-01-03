#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
from typing import List


# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i1 = 0
        i2 = 0
        res = []

        while i1 < len(nums1) and i2 < len(nums2):
            while i2 < len(nums2) and nums2[i2] < nums1[i1]:
                i2 += 1

            for i in range(i2, len(nums2)):
                res.append([nums1[i1], nums2[i]])

            i1 += 1

        res.sort(key=lambda a: a[0] + a[1])
        return res[:k]
# @lc code=end
