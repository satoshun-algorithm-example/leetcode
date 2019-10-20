#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
from typing import List


# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def move(x, y, land):
            if x >= len(grid[0]):
                return land
            if y >= len(grid):
                return land
            if grid[y][x] == 0:
                return land

            grid[y][x] = 0
            land += 1
            land = move(x - 1, y, land)
            land = move(x + 1, y, land)
            land = move(x, y + 1, land)
            land = move(x, y - 1, land)
            return land

        m = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                m = max(m, move(x, y, 0))
        return m

# @lc code=end
