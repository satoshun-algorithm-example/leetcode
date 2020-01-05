#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
from typing import List
import heapq


# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        res, heap = [], []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heapq.heappush(heap, [nums1[i] + nums2[j], nums1[i], nums2[j]])

            res.append(heapq.heappop(heap)[1:])
            if len(res) == k:
                return res

        while len(res) != k and heap:
            res.append(heapq.heappop(heap)[1:])

        return res
# @lc code=end
