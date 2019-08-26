#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            total = sum([int(i) * int(i) for i in str(n)])
            if 0 <= total <= 9:
                return total == 1 or total == 7
            n = total
