#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        return self.calculate(prices, 'cooldown', cache, 0)

    def calculate(self, prices, transaction, cache, profit):
        if not prices:
            return profit

        before_profit = cache.get((transaction, len(prices)))
        if before_profit and before_profit >= profit:
            return 0

        if transaction == 'buy':
            max_profit = max(
                profit,
                self.calculate(prices[2:], 'cooldown', cache, profit) + prices[0],
                self.calculate(prices[1:], 'buy', cache, profit)
            )
        else:
            max_profit = max(
                profit,
                self.calculate(prices[1:], 'buy', cache, profit) - prices[0],
                self.calculate(prices[1:], 'cooldown', cache, profit)
            )

        cache[(transaction, len(prices))] = profit
        return max_profit

# @lc code=end
