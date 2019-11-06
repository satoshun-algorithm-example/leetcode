#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#

# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0] * len(s1) for _ in s2]
        for i in range(1, len(s1)):
            dp[0][i] = dp[0][i - 1] + ord(s1[i])
        for i in range(1, len(s2)):
            dp[i][0] = dp[i - 1][0] + ord(s2[i])

        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                if s1[i] == s2[i]:
                    dp[j][i] = dp[j - 1][i - 1]
                else:
                    dp[j][i] = min(dp[j - 1][i] + ord(s2[j]), dp[j][i - 1] + ord(s1[i]))

        return dp[-1][-1]

# @lc code=end
