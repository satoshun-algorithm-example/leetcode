#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.calculate(prices, 'cooldown', 0)

    def calculate(self, prices, transaction, profit):
        if not prices:
            return profit

        if transaction == 'buy':
            return max(
                profit,
                self.calculate(prices[2:], 'cooldown', profit) + prices[0],
                self.calculate(prices[1:], 'buy', profit)
            )
        else:
            return max(
                profit,
                self.calculate(prices[1:], 'buy', profit) - prices[0],
                self.calculate(prices[1:], 'cooldown', profit)
            )

# @lc code=end
