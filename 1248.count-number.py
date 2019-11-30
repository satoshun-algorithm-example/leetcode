#
# @lc app=leetcode id=1248 lang=python3
#
from typing import List


# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [n % 2 for n in nums]

        def count_up(k):
            total = 0

            start, c = 0, 0
            n = 0
            for i in range(len(nums)):
                c += nums[i]
                n += 1
                while c > k:
                    c -= nums[start]
                    start += 1
                    n -= 1
                total += n
            return total

        return count_up(k) - count_up(k - 1)

# @lc code=end
