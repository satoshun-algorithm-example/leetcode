from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        nums.sort()

        while nums:
            start = nums.pop(0)
            for i in range(k - 1):
                try:
                    index = nums.index(start + 1)
                    start = nums.pop(index)
                except:
                    return False

        return True
