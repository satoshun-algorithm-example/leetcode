#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
from typing import List


# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for y in range(len(matrix)):
            for x in range(len(matrix[-1])):
                if matrix[y][x] == 0:
                    for xx in range(len(matrix[-1])):
                        if matrix[y][xx] == 1:
                            matrix[y][xx] = 2
                    for yy in range(len(matrix)):
                        if matrix[yy][x] == 1:
                            matrix[yy][x] = 2

        for y in range(len(matrix)):
            for x in range(len(matrix[-1])):
                if matrix[y][x] == 2:
                    matrix[y][x] = 0

# @lc code=end
