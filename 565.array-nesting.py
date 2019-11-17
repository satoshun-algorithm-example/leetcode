#
# @lc app=leetcode id=565 lang=python3
#
# [565] Array Nesting
#
from typing import List


# @lc code=start
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        m = 0
        for s in range(len(nums)):
            current = 0
            while nums[s] >= 0:
                current += 1
                nums[s], s = -1, nums[s]

            m = max(m, current)

        return m

# @lc code=end
