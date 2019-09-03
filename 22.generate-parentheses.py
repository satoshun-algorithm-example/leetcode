#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.parenthesis(n * 2, 0)

    def parenthesis(self, n, left_num):
        if n == 0:
            return []
        if left_num == n:
            return [')' * left_num]

        if left_num == 0:
            return ['(' + p for p in self.parenthesis(n - 1, left_num + 1)]

        return ['(' + p for p in self.parenthesis(n - 1, left_num + 1)] + \
               [')' + p for p in self.parenthesis(n - 1, left_num - 1)]
