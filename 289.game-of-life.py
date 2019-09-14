#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        c = board[:]
        ly = len(board)
        lx = len(board[0])
        for y in range(ly):
            for x in range(lx):
                lives = 0
                if y - 1 >= 0 and x - 1 >= 0:
                    lives += c[y - 1][x - 1]
                if y - 1 >= 0:
                    lives += c[y - 1][x]
                if y - 1 >= 0 and x + 1 < lx:
                    lives += c[y - 1][x + 1]
                if x - 1 >= 0:
                    lives += c[y][x - 1]
                if x + 1 < lx:
                    lives += c[y][x + 1]
                if y + 1 < ly and x - 1 >= 0:
                    lives += c[y + 1][x - 1]
                if y + 1 < ly:
                    lives += c[y + 1][x]
                if y + 1 < ly and x + 1 < lx:
                    lives += c[y + 1][x + 1]

                if c[y][x]:
                    if lives == 2 or lives == 3:
                        pass
                    else:
                        board[y][x] = 0
                else:
                    if lives == 3:
                        board[y][x] = 1
