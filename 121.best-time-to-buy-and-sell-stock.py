#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, profit = float('inf'), 0

        for price in prices:
            low = min(price, low)
            profit = max(profit, price - low)

        return profit
