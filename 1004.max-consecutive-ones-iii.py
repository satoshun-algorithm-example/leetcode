#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
from typing import List


# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start, res = 0, 0

        for end in range(len(A)):
            if A[end] == 0:
                K -= 1

            while K < 0:
                if A[start] == 0:
                    K += 1
                start += 1

            res = max(res, end - start + 1)

        return res

# @lc code=end
