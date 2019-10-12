#
# @lc app=leetcode id=807 lang=python3
#
# [807] Max Increase to Keep City Skyline
#
from typing import List


# @lc code=start
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                total += min(
                    max(grid[y1][x] for y1 in range(len(grid))),
                    max(grid[y][x1] for x1 in range(len(grid[0]))),
                ) - grid[y][x]

        return total

# @lc code=end
