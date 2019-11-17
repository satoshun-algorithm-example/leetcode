from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for _ in range(k):
            for y in range(len(grid)):
                tmp = grid[y][-1]
                for x in range(len(grid[0])):
                    tmp, grid[y][x] = grid[y][x], tmp

            tmp = grid[-1][0]
            for y in range(len(grid)):
                tmp, grid[y][0] = grid[y][0], tmp

        return grid
