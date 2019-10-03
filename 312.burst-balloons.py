#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
from typing import List


# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        s = "".join(("0" for _ in range(len(nums))))
        return self.search(nums, 0, s, cache)

    def search(self, nums, value, consumed, cache):
        if cache.get(consumed, -1) >= value:
            return value
        cache[consumed] = value

        m = value
        for i in range(len(nums)):
            if consumed[i] == "1":
                continue

            left = 1
            j = i
            while j - 1 >= 0:
                if consumed[j - 1] == '0':
                    left = nums[j - 1]
                    break
                j -= 1

            right = 1
            j = i
            while j + 1 < len(nums):
                if consumed[j + 1] == '0':
                    right = nums[j + 1]
                    break
                j += 1

            point = left * nums[i] * right
            m = max(m, self.search(nums, value + point, consumed[:i] + '1' + consumed[i + 1:], cache))

        return m
# @lc code=end
