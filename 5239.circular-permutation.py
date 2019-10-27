#
# @lc app=leetcode id=5239 lang=python3
#
# [5239]
#

# @lc code=start
from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        result = ["0", "1"]

        for _ in range(1, n):
            n = len(result)
            is_zero = True
            for i in range(n):
                index = i * 2
                if is_zero:
                    e = result[index]
                    result[index] = "0" + e
                    result.insert(index + 1, "1" + e)
                    is_zero = False
                else:
                    e = result[index]
                    result[index] = "1" + e
                    result.insert(index + 1, "0" + e)
                    is_zero = True

        result = [int(s, 2) for s in result]
        i = result.index(start)

        return result[i:] + result[:i]

# @lc code=end
