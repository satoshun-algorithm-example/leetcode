#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        s = sorted(d.items(), key=lambda a: a[1], reverse=True)[:k]
        return list(map(lambda a: a[0], s))
