#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []

        rs = [[1]]
        for i in range(1, numRows):
            rb = rs[i - 1]
            r = []

            for j in range(i + 1):
                if j == 0 or j == i:
                    r.append(1)
                else:
                    r.append(rb[j] + rb[j - 1])

            rs.append(r)

        return rs
