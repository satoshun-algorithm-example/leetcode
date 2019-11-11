#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#
from typing import List


# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            d = 1
            current = 0
            for weight in weights:
                current += weight
                if current > mid:
                    d += 1
                    current = weight

            if d > D:
                left = mid + 1
            else:
                right = mid

        return left

# @lc code=end
