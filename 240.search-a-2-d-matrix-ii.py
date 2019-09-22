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
                v = matrix[y][x]
                if v == target:
                    return True
                if target < v:
                    break

        return False
