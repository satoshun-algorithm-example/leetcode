#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#
from typing import List


# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        i = 0
        chunks = 0
        while i < len(arr):
            chunks += 1
            i = arr[i] + 1

        return chunks

# @lc code=end
