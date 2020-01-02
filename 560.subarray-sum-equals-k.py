#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = {0: 1}

        res = 0
        total = 0
        for num in nums:
            total += num
            res += cache.get(total - k, 0)
            cache[total] = cache.get(total, 0) + 1

        return res
