#
# @lc app=leetcode id=565 lang=python3
#
# [565] Array Nesting
#
from typing import List


# @lc code=start
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = {}
        m = 0
        for s in range(len(nums)):
            if s in visited:
                continue

            current = 0
            while s not in visited:
                current += 1
                visited[s] = True
                s = nums[s]

            m = max(m, current)

        return m

# @lc code=end
