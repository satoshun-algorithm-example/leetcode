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
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == target:
                    return True

        return False
