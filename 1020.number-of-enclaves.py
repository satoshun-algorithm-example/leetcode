#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#
from typing import List


# @lc code=start
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        def fill_zero(x, y):
            try:
                if A[y][x] != 1:
                    return
            except:
                return

            A[y][x] = 0
            fill_zero(x - 1, y)
            fill_zero(x + 1, y)
            fill_zero(x, y - 1)
            fill_zero(x, y + 1)

        # top and bottom
        for x in range(len(A[0])):
            if A[0][x] == 1:
                fill_zero(x, 0)
            if A[len(A) - 1][x] == 1:
                fill_zero(x, len(A) - 1)

        # left and right
        for y in range(len(A)):
            if A[y][0] == 1:
                fill_zero(0, y)
            if A[y][len(A[0]) - 1] == 1:
                fill_zero(len(A[0]) - 1, y)

        return sum(sum(a) for a in A)
# @lc code=end
