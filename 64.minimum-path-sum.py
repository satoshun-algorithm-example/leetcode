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
        while True:
            i, j = 0, 0
            m = sys.maxsize
            for y in range(ym):
                for x in range(xm):
                    if board[y][x] != -1 and board[y][x] < m:
                        i, j = y, x
                        m = board[y][x]

            if i == ym - 1 and j == xm - 1:
                return m

            board[i][j] = -1

            if j + 1 < xm and m + grid[i][j + 1] < board[i][j + 1]:
                board[i][j + 1] = m + grid[i][j + 1]
            if i + 1 < ym and m + grid[i + 1][j] < board[i + 1][j]:
                board[i + 1][j] = m + grid[i + 1][j]
