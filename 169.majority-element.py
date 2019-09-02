#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            if n not in m:
                m[n] = 0
            m[n] += 1
            if m[n] > (len(nums) // 2):
                return n

        return max(m.items(), key=lambda x: x[1])[0]
