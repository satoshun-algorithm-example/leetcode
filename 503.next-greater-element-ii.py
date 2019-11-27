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
        stack = []
        for i in range(len(nums) * 2):
            n = i % len(nums)
            num = nums[n]
            while len(stack) != 0 and nums[stack[-1]] < num:
                result[stack.pop()] = num

            if i == n:
                stack.append(i)

        return result
# @lc code=end
