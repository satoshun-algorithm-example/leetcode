#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        row, col = len(matrix[0]) - 1, 0
        while row >= 0 and col < len(matrix):
            if matrix[col][row] == target:
                return True
            elif matrix[col][row] > target:
                row -= 1
            else:
                col += 1

        return False
