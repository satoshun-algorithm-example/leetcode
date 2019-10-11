#
# @lc app=leetcode id=861 lang=python3
#
# [861] Score After Flipping Matrix
#

from typing import List


# @lc code=start
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for col in range(len(A)):
            if A[col][0] == 0:
                for row in range(len(A[0])):
                    A[col][row] = 0 if A[col][row] else 1

        for row in range(1, len(A[0])):
            c0 = 0
            c1 = 0
            for col in range(len(A)):
                if A[col][row] == 0:
                    c0 += 1
                else:
                    c1 += 1
            if c0 > c1:
                for col in range(len(A)):
                    A[col][row] = 0 if A[col][row] else 1

        c = 0
        for a in A:
            c += int("".join(map(str, a)), 2)

        print(A)
        return c
# @lc code=end
