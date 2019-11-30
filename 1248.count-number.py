#
# @lc app=leetcode id=1248 lang=python3
#
from typing import List


# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        total = 0

        start, c = 0, 0
        n = 0
        # calculate k sub array
        for i in range(len(nums)):
            c += nums[i] % 2
            n += 1
            while c > k:
                c -= nums[start] % 2
                start += 1
                n -= 1
            total += n

        start, c = 0, 0
        n = 0
        # calculate k - 1 sub array
        for i in range(len(nums)):
            c += nums[i] % 2
            n += 1
            while c > k - 1:
                c -= nums[start] % 2
                start += 1
                n -= 1
            total -= n

        return total

# @lc code=end
