#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#
from typing import List


# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0

        diffs = [1]
        diff = A[1] - A[0]
        for i in range(2, len(A)):
            if diff == A[i] - A[i - 1]:
                diffs[-1] += 1
            else:
                diffs.append(1)
                diff = A[i] - A[i - 1]

        total = 0
        for diff in diffs:
            total += sum(d for d in range(diff))

        return total

# @lc code=end
