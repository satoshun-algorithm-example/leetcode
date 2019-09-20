#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, cur, res = {0: 1}, 0, 0
        for num in nums:
            cur += num
            res += count.get(cur - k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res
