#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#
from typing import List


# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        start = 0
        end = len(nums) - 1
        n = (end + 1 - start) // 2
        while True:
            pivot = nums[n]
            if nums[n - 1] == pivot:
                end = n - 2
            else:
                start = n + 2

            n = (end + 1 - start) // 2

            if end - start == 2:
                pivot = nums[n]
                if nums[n - 1] == pivot:
                    return n + 1
                else:
                    return n - 1

# @lc code=end
