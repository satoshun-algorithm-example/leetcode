#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(cur: int):
            if cur == 0:
                return 0
            if cur == 1:
                return 1
            if cur == 2:
                return 2
            return climb(cur - 1) + climb(cur - 2)

        return climb(n)
