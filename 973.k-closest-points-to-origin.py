#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
from typing import List


# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda point: point[0] ** 2 + point[1] ** 2)[:K]

# @lc code=end
