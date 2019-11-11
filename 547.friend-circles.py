#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#
from typing import List


# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        total = 0
        visited = set()

        def visit(index):
            if index in visited:
                return
            visited.add(index)
            for k in range(len(M[index])):
                if M[index][k] == 1:
                    visit(k)

        for i in range(len(M)):
            if i not in visited:
                visit(i)
                total += 1

        return total

# @lc code=end
