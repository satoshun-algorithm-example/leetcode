#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}

        def climb(cur: int):
            if cur == 0:
                return 0
            if cur == 1:
                return 1
            if cur == 2:
                return 2
            v = d.get(cur, None)
            if v:
                return v
            v = climb(cur - 1) + climb(cur - 2)
            d[cur] = v
            return v

        return climb(n)
