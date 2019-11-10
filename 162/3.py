from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        total = 0
        len_x = len(grid[0])
        len_y = len(grid)

        def closed(y, x):
            if x == 0 or x >= len_x - 1:
                return False
            if y == 0 or y >= len_y - 1:
                return False

            grid[y][x] = 1
            is_land = True
            if grid[y][x - 1] == 0:
                is_land = is_land and closed(y, x - 1)
            if grid[y][x + 1] == 0:
                is_land = is_land and closed(y, x + 1)
            if grid[y - 1][x] == 0:
                is_land = is_land and closed(y - 1, x)
            if grid[y + 1][x] == 0:
                is_land = is_land and closed(y + 1, x)

            return is_land

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    if closed(y, x):
                        total += 1

        return total
