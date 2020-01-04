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
        res = [[nums1[i1], nums1[i2]]]

        for i in range(k):
            if i1 >= len(nums1):
                res.append([nums1[i1], nums2[i2 + 1]])
                i2 += 1
                continue
            if i2 >= len(nums2):
                res.append([nums1[i1 + 1], nums2[i2]])
                i1 += 1
                continue

            if nums1[i1 + 1] + nums2[i2] < nums1[i1] + nums2[i2 + 1]:
                res.append([nums1[i1 + 1], nums2[i2]])
                i1 += 1
            else:
                res.append([nums1[i1], nums2[i2 + 1]])
                i2 += 1

        return res
# @lc code=end
