#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
from typing import List


# @lc code=start
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]

        res = []
        for i in range(len(input)):
            if input[i] in '-+*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        if input[i] == '-':
                            res.append(l - r)
                        elif input[i] == '+':
                            res.append(l + r)
                        else:
                            res.append(l * r)

        return res

# @lc code=end
