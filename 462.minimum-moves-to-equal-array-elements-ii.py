#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#
from typing import List


# @lc code=start
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        start = 0
        end = len(nums) - 1
        while len(nums) > start + 1 and nums[start] == nums[start + 1]:
            start += 1
        while end >= 0 and nums[end] == nums[end - 1]:
            end -= 1

        while start < end:
            diff_end = len(nums) - 1 - end
            if start > diff_end:
                nums[end] -= 1
                count += diff_end + 1
            else:
                nums[start] += 1
                count += start + 1

            while len(nums) > start + 1 and nums[start] == nums[start + 1]:
                start += 1
            while end > 0 and nums[end] == nums[end - 1]:
                end -= 1

        return count

# @lc code=end
