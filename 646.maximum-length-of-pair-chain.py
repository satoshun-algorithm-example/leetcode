#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#
from typing import List


# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda a: a[1])
        dp = [1 for _ in pairs]
        for i in range(1, len(pairs)):
            dp[i] = max(dp)
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1]

# @lc code=end
