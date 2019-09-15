#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
from typing import List
import sys


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ym = len(grid)
        xm = len(grid[0])

        board = [[sys.maxsize] * xm for _ in range(ym)]

        board[0][0] = grid[0][0]
        queue = [(grid[0][0], 0, 0)]
        while True:
            q = queue.pop(0)

            m, i, j = q[0], q[1], q[2]
            if q[1] == ym - 1 and q[2] == xm - 1:
                return q[0]

            if j + 1 < xm and m + grid[i][j + 1] < board[i][j + 1]:
                board[i][j + 1] = m + grid[i][j + 1]
                queue.append((board[i][j + 1], i, j + 1))
            if i + 1 < ym and m + grid[i + 1][j] < board[i + 1][j]:
                board[i + 1][j] = m + grid[i + 1][j]
                queue.append((board[i + 1][j], i + 1, j))

            queue.sort()
