#
# @lc app=leetcode id=1248 lang=python3
#
from typing import List


# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        c = 0
        nums = [n % 2 for n in nums]
        for i in range(len(nums)):
            odd = 0
            for j in range(i, -1, -1):
                if nums[j] == 1:
                    odd += 1

                if odd > k:
                    break

                if odd == k:
                    c += 1

        return c
# @lc code=end
