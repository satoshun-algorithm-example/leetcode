#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#
from typing import List


# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        m = 0
        for i in range(len(arr)):
            m = max(arr[i], m)
            if m == i:
                chunks += 1

        return chunks

# @lc code=end
