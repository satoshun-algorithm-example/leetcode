#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#
from typing import List


# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        capacity = max(weights)

        while True:
            d = 1
            current = 0
            for weight in weights:
                current += weight
                if current > capacity:
                    d += 1
                    current = weight

            if d <= D:
                break
            capacity += 1

        return capacity

# @lc code=end
