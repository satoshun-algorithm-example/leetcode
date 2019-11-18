#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#
from typing import List


# @lc code=start
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maximums = []
        l = 0
        for n in nums:
            digits = len(f"{n:b}")
            if digits == l:
                maximums.append(n)
            elif digits > l:
                l = digits
                maximums.clear()
                maximums.append(n)

        m = 0
        for maximum in maximums:
            for num in nums:
                if num == maximum:
                    continue
                m = max(m, num ^ maximum)

        return m

# @lc code=end
