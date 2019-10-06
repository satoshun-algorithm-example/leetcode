#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#
from typing import List


# @lc code=start
class Solution:
    def isToeplitzMatrix(self, materix: List[List[int]]) -> bool:
        for y in range(len(materix)):
            base = materix[y][0]
            for x in range(1, len(materix[0])):
                if y + x >= len(materix):
                    break
                if materix[y + x][x] != base:
                    return False

        for x in range(len(materix[0])):
            base = materix[0][x]
            for y in range(1, len(materix)):
                if x + y >= len(materix[0]):
                    break
                if materix[y][x + y] != base:
                    return False

        return True
# @lc code=end
