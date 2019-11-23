#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
from typing import List


# @lc code=start
class Solution:
    def diffWaysToCompute(self, input: str, memo=None) -> List[int]:
        if memo is None:
            memo = {}

        if input.isdigit():
            return [int(input)]

        if input in memo:
            return memo[input]

        res = []
        for i in range(len(input)):
            if input[i] in '-+*':
                left = self.diffWaysToCompute(input[:i], memo)
                right = self.diffWaysToCompute(input[i + 1:], memo)
                for l in left:
                    for r in right:
                        if input[i] == '-':
                            res.append(l - r)
                        elif input[i] == '+':
                            res.append(l + r)
                        else:
                            res.append(l * r)

        memo[input] = res
        return res

# @lc code=end
