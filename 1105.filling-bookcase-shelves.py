#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#
from typing import List
import sys


# @lc code=start
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        dp = [sys.maxsize] * (len(books) + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            width = books[i - 1][0]
            height = books[i - 1][1]
            dp[i] = dp[i - 1] + height

            j = i - 1
            while j > 0 and width + books[j - 1][0] <= shelf_width:
                height = max(height, books[j - 1][1])
                width += books[j - 1][0]
                dp[i] = min(dp[i], dp[j - 1] + height)
                j -= 1

        return dp[-1]

# @lc code=end
