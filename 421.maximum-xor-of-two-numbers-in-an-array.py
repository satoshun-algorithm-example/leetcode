#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#
from typing import List


# @lc code=start
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        m = 0
        mask = 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            values = {num & mask for num in nums}
            candidate_max = m | (1 << i)
            for prefix in values:
                if (candidate_max ^ prefix) in values:
                    m = candidate_max
                    break

        return m

# @lc code=end
