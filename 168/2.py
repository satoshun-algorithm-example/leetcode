from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        for key in sorted(d.keys()):
            while d[key]:
                for i in range(key, key + k):
                    if d.get(i, 0) == 0:
                        return False
                    d[i] -= 1

        return True
