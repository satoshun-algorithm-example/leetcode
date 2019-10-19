#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#
from typing import List


# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_index = 0
        for push in pushed:
            if popped[pop_index] == push:
                pop_index += 1
                while stack and stack[-1] == popped[pop_index]:
                    stack.pop()
                    pop_index += 1
                continue

            stack.append(push)

        return not stack

# @lc code=end
