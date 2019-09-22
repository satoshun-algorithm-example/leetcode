#
# @lc app=leetcode id=1103 lang=python3
#
# [1103] Distribute Candies to People
#
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        value = 1
        while candies > 0:
            res[(value - 1) % num_people] += min(candies, value)
            candies -= value
            value += 1

        return res
