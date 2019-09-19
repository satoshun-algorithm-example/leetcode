#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ylen = len(grid)
        xlen = len(grid[0])
        c = 0
        for y in range(ylen):
            for x in range(xlen):
                if grid[y][x] == '1':
                    self.fill(grid, x, y, xlen, ylen)
                    c += 1
        return c

    def fill(self, grid, x, y, xlen, ylen):
        grid[y][x] = '0'
        if x > 0:
            if grid[y][x - 1] == '1':
                self.fill(grid, x - 1, y, xlen, ylen)
        if x + 1 < xlen:
            if grid[y][x + 1] == '1':
                self.fill(grid, x + 1, y, xlen, ylen)
        if y > 0:
            if grid[y - 1][x] == '1':
                self.fill(grid, x, y - 1, xlen, ylen)
        if y + 1 < ylen:
            if grid[y + 1][x] == '1':
                self.fill(grid, x, y + 1, xlen, ylen)
