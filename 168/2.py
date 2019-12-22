from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        if len(nums) % k != 0:
            return False

        while nums:
            start = nums.pop(0)
            for i in range(k - 1):
                find = False
                for j in range(len(nums)):
                    if nums[j] == start + 1:
                        start = nums.pop(j)
                        find = True
                        break

                if not find:
                    return False

        return True
