#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for x in range(len(matrix)):
            for y in range(len(matrix)):
                matrix[x][y] = matrix[n - 1 - y][x]
