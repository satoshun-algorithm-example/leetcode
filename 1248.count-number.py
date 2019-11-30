#
# @lc app=leetcode id=1248 lang=python3
#
from typing import List


# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [n % 2 for n in nums]

        def count_up(k):
            total, start = 0, 0
            for i in range(len(nums)):
                k -= nums[i]
                while k < 0:
                    k += nums[start]
                    start += 1
                total += i - start + 1
            return total

        return count_up(k) - count_up(k - 1)

# @lc code=end
