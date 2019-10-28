#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#
from builtins import enumerate
from typing import List


# @lc code=start
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {day: 0 for day in days}
        dp[0] = 0

        for i, day in enumerate(days):
            if i == 0:
                c1 = costs[0]
                c2 = costs[1]
                c3 = costs[2]
            else:
                c1 = dp[i - 1] + costs[0]

                ci2 = min(i - 6, 0)
                while dp.get(ci2) is None:
                    ci2 += 1
                c2 = dp[ci2] + costs[1]

                ci3 = min(i - 29, 0)
                while dp.get(ci3) is None:
                    ci3 += 1
                c3 = dp[ci3] + costs[2]

            dp[i] = min(c1, c2, c3)

        return dp[days[-1]]

# @lc code=end
