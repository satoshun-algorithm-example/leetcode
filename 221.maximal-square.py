#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                matrix[y][x] = int(matrix[y][x])

        m = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                m = max(m, self.calculate(matrix, y, x))

        return m

    def calculate(self, matrix, y, x):
        n = 1
        while True:
            a = 0
            for yy in range(y):
                a += sum(matrix[yy][x: x + n])
            if a != (n ** 2):
                break
            n += 1

        return (n - 1) ** 2
