#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#

# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
        for i in range(1, len(s1) + 1):
            dp[0][i] = dp[0][i - 1] + ord(s1[i - 1])
        for j in range(1, len(s2) + 1):
            dp[j][0] = dp[j - 1][0] + ord(s2[j - 1])

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1]
                else:
                    dp[j][i] = min(dp[j - 1][i] + ord(s2[j - 1]), dp[j][i - 1] + ord(s1[i - 1]))

        return dp[-1][-1]

# @lc code=end
