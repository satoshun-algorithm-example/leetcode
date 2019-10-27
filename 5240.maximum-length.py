#
# @lc app=leetcode id=5240 lang=python3
#
# [5240]
#

# @lc code=start
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def calculate(current, start):
            if len(current) != len(set(current)):
                return 0

            if start == len(arr):
                return len(current)

            return max(calculate(current + arr[start], start + 1), calculate(current, start + 1))

        return calculate("", 0)

# @lc code=end
