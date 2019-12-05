#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
from typing import List


# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        dx, dy = 1, 0
        x, y = 0, 0
        matrix[0][0] = 1
        for i in range(1, n ** 2):
            if n <= x + dx or n <= y + dy or (matrix[y+dy][x+dx]):
                dx, dy = -dy, dx
            x += dx
            y += dy
            matrix[y][x] = i + 1
        return matrix

# @lc code=end
