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
        tmp = matrix[0][2]
        matrix[0][2] = matrix[0][0]

        tmp2 = matrix[2][2]
        matrix[2][2] = tmp

        tmp3 = matrix[2][0]
        matrix[2][0] = tmp2

        matrix[0][0] = tmp3

        tmp = matrix[1][2]
        matrix[1][2] = matrix[0][1]

        tmp2 = matrix[2][1]
        matrix[2][1] = tmp

        tmp3 = matrix[1][0]
        matrix[1][0] = tmp2

        matrix[0][1] = tmp3
