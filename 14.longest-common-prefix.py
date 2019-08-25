#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        short = min(strs, key=len)
        for i in range(len(short)):
            for s in strs:
                if s[i] != short[i]:
                    return short[:i]

        return short
