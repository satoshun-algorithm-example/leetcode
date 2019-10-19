#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
from typing import List


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff ^= num

        mask = 1
        while True:
            if (mask & diff) != 0:
                break
            mask = mask << 1

        a, b = 0, 0
        for num in nums:
            if (num & mask) == 0:
                a ^= num
            else:
                b ^= num

        return [a, b]

# @lc code=end
