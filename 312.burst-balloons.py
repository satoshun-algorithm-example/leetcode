#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
from typing import List


# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [num for num in nums if num > 0] + [1]
        cache = [[0] * len(nums) for _ in range(len(nums))]
        return self.search(nums, 0, len(nums) - 1, cache)

    def search(self, nums, left, right, cache):
        if left + 1 == right:
            return 0
        if cache[left][right] > 0:
            return cache[left][right]

        value = 0
        for i in range(left + 1, right):
            d = nums[left] * nums[i] * nums[right]
            value = max(
                value,
                self.search(nums, left, i, cache) + d + self.search(nums, i, right, cache))

        cache[left][right] = value
        return value
# @lc code=end
