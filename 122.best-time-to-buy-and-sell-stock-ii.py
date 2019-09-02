#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        s = None

        for i, p in enumerate(prices):
            if s is None:
                if len(prices) == i + 1:
                    break
                if prices[i] < prices[i + 1]:
                    s = prices[i]
            else:
                if s < prices[i] and (len(prices) == i + 1 or prices[i] > prices[i + 1]):
                    profit += prices[i] - s
                    s = None

        return profit
