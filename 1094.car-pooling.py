#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#
from typing import List


# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda a: a[1])

        passengers = [0] * max(trip[2] for trip in trips)
        for trip in trips:
            for i in range(trip[1], trip[2]):
                passengers[i] += trip[0]
                if passengers[i] > capacity:
                    return False

        return True

# @lc code=end
