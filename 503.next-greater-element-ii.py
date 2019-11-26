#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
from typing import List


# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i, n in enumerate(nums):
            greater = -1

            # current -> end
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    greater = nums[j]
                    break
            if greater != -1:
                result[i] = greater
                continue

            for j in range(i):
                if nums[i] < nums[j]:
                    greater = nums[j]
                    break

            result[i] = greater

        return result
# @lc code=end
