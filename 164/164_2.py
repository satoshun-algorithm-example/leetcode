from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        count = 0

        def fill_and_count(y, x):
            # no server
            if grid[y][x] == 0:
                return 0

            grid[y][x] = 0

            c = 1
            for row in range(len(grid[0])):
                c += fill_and_count(y, row)
            for column in range(len(grid)):
                c += fill_and_count(column, x)

            return c

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                c = fill_and_count(y, x)
                if c > 1:
                    count += c

        return count
