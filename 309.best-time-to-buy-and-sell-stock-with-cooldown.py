#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        rest = [0 for _ in range(len(prices))]
        buy = [0 for _ in range(len(prices))]
        down = [0 for _ in range(len(prices))]

        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            rest[i] = max(rest[i - 1], down[i - 1])
            buy[i] = max(buy[i - 1], rest[i - 1] - prices[i])
            down[i] = buy[i - 1] + prices[i]

        return max(rest[-1], down[-1])

# @lc code=end
