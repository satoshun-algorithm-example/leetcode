#
# @lc app=leetcode id=5230 lang=python3
#
# [5230]
#
from typing import List


# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        if len(coordinates) <= 2:
            return True
        x = coordinates[1][0] - coordinates[0][0]
        y = coordinates[1][1] - coordinates[0][1]

        first = coordinates[0]
        for coordinate in coordinates[2:]:
            x1 = coordinate[0] - first[0]
            y1 = coordinate[1] - first[1]
            if x == 0:
                if x1 != 0:
                    return False
            elif y == 0:
                if y1 != 0:
                    return False
            else:
                if x1 == 0:
                    return False
                if y1 == 0:
                    return False
                if (x / y) != (x1 / y1):
                    return False

        return True

# @lc code=end
