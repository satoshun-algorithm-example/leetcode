#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dfs = [0 for _ in range(len(prices))]
        for i in range(len(prices)):
            pass

        return dfs[-1]
# @lc code=end
