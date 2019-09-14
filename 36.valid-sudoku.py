#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i][:9]
            if len(set(row)) + row.count('.') - 1 != 9:
                return False

            column = []
            for j in range(9):
                column.append(board[j][i])
            if len(set(column)) + column.count('.') - 1 != 9:
                return False

        for y in range(1, 9, 3):
            for x in range(1, 9, 3):
                b = board[y - 1][x - 1:x + 2] + board[y][x - 1:x + 2] + board[y + 1][x - 1:x + 2]
                if len(set(b)) + b.count('.') - 1 != 9:
                    return False

        return True
