#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * len(text1)

        for c in reversed(text2):
            for i in range(len(text1)):
                if text1[i] == c:
                    dp[i] = max(dp[i:]) + 1

        return max(dp)

# @lc code=end
