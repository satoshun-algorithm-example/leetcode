#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
from typing import List


# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        for i, n in enumerate(nums):
            greater = False

            # current -> end
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    result[i] = nums[j]
                    greater = True
                    break
            if greater:
                continue

            for j in range(i):
                if nums[i] < nums[j]:
                    result[i] = nums[j]
                    break

        return result
# @lc code=end
