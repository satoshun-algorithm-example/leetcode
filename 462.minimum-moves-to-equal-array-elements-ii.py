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
            diff_start = (start + 1) * (nums[start + 1] - nums[start])
            diff_end = (len(nums) - end) * (nums[end] - nums[end - 1])
            if diff_start > diff_end:
                end -= 1
                count += diff_end
            else:
                start += 1
                count += diff_start

            while len(nums) > start + 1 and nums[start] == nums[start + 1]:
                start += 1
            while end > 0 and nums[end] == nums[end - 1]:
                end -= 1

        return count

# @lc code=end
