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
        advance = 0
        current = 1
        while current <= n ** 2:
            for x in range(advance, n - advance):
                matrix[advance][x] = current
                current += 1
            for y in range(advance + 1, n - advance):
                matrix[y][n - advance - 1] = current
                current += 1
            for x in range(n - advance - 2, advance - 1, - 1):
                matrix[n - advance - 1][x] = current
                current += 1
            for y in range(n - advance - 2, advance, -1):
                matrix[y][advance] = current
                current += 1
            advance += 1

        return matrix

# @lc code=end
