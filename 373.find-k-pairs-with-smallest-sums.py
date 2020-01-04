#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
from typing import List


# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        heap = []

        if not nums1 or not nums2:
            return res

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heap.append([nums1[i], nums2[j]])

            heap.sort(key=lambda a: a[0] + a[1])
            res.append(heap.pop(0))
            if len(res) == k:
                return res

        while len(res) != k and heap:
            res.append(heap.pop(0))

        return res
# @lc code=end
